# coding=utf-8
"""Deal with job-related APIs."""
from flask import request
from flask_restplus import Namespace, Resource
from flask_login import login_required, current_user
from ..model import jobs, images
from .utils import get_message_json, handle_internal_error, HTTPStatus, ConstantCodes, DBErrorCodes, convert_to_int
from sqlalchemy.exc import IntegrityError

api = Namespace('jobs')


@api.route('/<int:job_id>')
class JobResource(Resource):
    """Deal with single job."""

    @login_required
    def get(self, job_id):
        """Retrieve a single job by id."""
        try:
            result = jobs.find_job_by_id(job_id)

            if len(result) == 1:
                result = result[0]
            else:
                return get_message_json('任务不存在'), HTTPStatus.NOT_FOUND

            # Admin can retrieve any job,
            # while others can only retrieve his own job
            if not current_user.is_admin() and result.account_id != current_user.account_id:
                return get_message_json('用户无法访问他人任务'), HTTPStatus.FORBIDDEN

            json_res = result.to_json()
            json_res['message'] = '成功查看任务'
            return json_res, HTTPStatus.OK

        except Exception as err:
            return handle_internal_error(str(err))

    @login_required
    @api.doc(parser=api.parser()
             .add_argument('body', type=str, required=True, help='json', location='json')
            )
    def put(self, job_id):
        """Edit a single job by id."""
        form = request.get_json()
        if form['account_id'] != current_user.account_id:
            return get_message_json('用户无法修改他人任务'), HTTPStatus.FORBIDDEN
        try:
            previous_job = jobs.find_job_by_id(job_id)
            if len(previous_job) == 1:
                previous_job = previous_job[0]
            else:
                return get_message_json('任务不存在'), HTTPStatus.NOT_FOUND

            if previous_job.job_state == ConstantCodes.Finished:
                return get_message_json('用户无法修改已完成的任务'), HTTPStatus.FORBIDDEN

            if images.find_image_by_id(form['image_id']).image_state == ConstantCodes.Done:
                return get_message_json('指定的图像已完成标注'), HTTPStatus.BAD_REQUEST

            result = jobs.update_job_by_id(
                job_id,
                form['image_id'],
                form['account_id'],
                form['label_id'],
                form['finished_date'],
                form['job_state'],
            )
            if result == 1:
                json_res = form.copy()
                json_res['message'] = '成功编辑任务'
                # Check whether to update corresponding image
                if form['job_state'] == ConstantCodes.Finished:
                    jobs_of_same_image = jobs.find_job_by_image_id(form['image_id'])
                    images.update_image_state(form['image_id'], jobs_of_same_image)

                return json_res, HTTPStatus.OK
            else:
                return get_message_json('未知的任务更新失败'), HTTPStatus.BAD_REQUEST

        except IntegrityError as err:
            if err.orig.args[0] == DBErrorCodes.FOREIGN_KEY_FAILURE:
                return get_message_json('指定的用户或图像不存在'), HTTPStatus.BAD_REQUEST
            else:
                return handle_internal_error(err.orig.args[1])
        except Exception as err:
            return handle_internal_error(str(err))

    @login_required
    def delete(self, job_id):
        """Delete a single job by id."""
        # Only admin can delete any job
        if not current_user.is_admin():
            return get_message_json('删除任务需要管理员权限'), HTTPStatus.FORBIDDEN

        try:
            result = jobs.delete_job_by_id(job_id)
            if result == 1:
                return get_message_json('已删除该任务'), HTTPStatus.OK
            else:
                if len(jobs.find_job_by_id(job_id)) == 0:
                    return get_message_json('任务不存在'), HTTPStatus.NOT_FOUND
                return get_message_json('未知的任务删除失败'), HTTPStatus.BAD_REQUEST
        except Exception as err:
            return handle_internal_error(str(err))


@api.route('/')
class JobsCollectionResource(Resource):
    """Deal with collection of jobs."""

    @login_required
    @api.doc(parser=api.parser()
             .add_argument('image_id', type=str, required=False, help='id of image', location='args')
             .add_argument('account_id', type=str, required=False, help='id of account', location='args')
             .add_argument('job_state', type=str, required=False, help='state of job', location='args')
            )
    def get(self):
        """List all jobs."""
        # These arguments are all strings originally and should be cast to int
        account_id = convert_to_int(request.args.get('account_id'))
        image_id = convert_to_int(request.args.get('image_id'))
        job_state = convert_to_int(request.args.get('job_state'))

        if not current_user.is_admin()\
                and (account_id is None or account_id != current_user.account_id):
            return get_message_json('用户没有权限访问其他用户的任务列表'), HTTPStatus.FORBIDDEN

        try:
            result = jobs.find_all_jobs(account_id, image_id, job_state)

            if len(result) == 0:
                return get_message_json('没有符合查询条件的任务'), HTTPStatus.NOT_FOUND

            data = []
            for job in result:
                data.append(job.to_json())
            json_res = {
                'message': '成功获取所有任务',
                'data': data
            }
            return json_res, HTTPStatus.OK
        except Exception as err:
            return handle_internal_error(str(err))

    @login_required
    @api.doc(parser=api.parser()
             .add_argument('body', type=str, required=True, help='json', location='json')
            )
    def post(self):
        """Create a job."""
        form = request.get_json()
        # Only admin can create jobs
        if not current_user.is_admin():
            return get_message_json('创建任务需要管理员权限'), HTTPStatus.FORBIDDEN
        
        try:
            # Finished image can not be assigned
            if images.find_image_by_id(form['image_id']).image_state == ConstantCodes.Done:
                return get_message_json('指定的图像已完成标注'), HTTPStatus.BAD_REQUEST

            result = jobs.add_job(
                form['image_id'],
                form['account_id']
            )
            json_res = result.to_json()
            json_res['message'] = '任务创建成功'

            # Modify the state of the image
            images.update_image_by_id(form['image_id'], _image_state=ConstantCodes.Running)

            return json_res, HTTPStatus.CREATED

        except IntegrityError as err:
            if err.orig.args[0] == DBErrorCodes.FOREIGN_KEY_FAILURE:
                return get_message_json('指定的用户或图像不存在'), HTTPStatus.BAD_REQUEST
            else:
                return handle_internal_error(err.orig.args[1])
        except Exception as err:
            return handle_internal_error(str(err))
