# coding=utf-8
"""Deal with job-related APIs."""
from flask import request
from flask_restplus import Namespace, Resource
from flask_login import login_required, current_user
from ..model import jobs, accounts
from .utils import get_message_json, handle_internal_error, HTTPStatus

api = Namespace('jobs')


@api.route('/<int:job_id>')
class JobResource(Resource):
    """Deal with single job."""

    @login_required
    def get(self, job_id):
        """Retrieve a single job by id."""
        try:
            result = jobs.find_job_by_id(job_id)
        except Exception as err:
            return handle_internal_error(str(err))

        if len(result) == 1:
            result = result[0]
        else:
            return get_message_json('该任务不存在'), HTTPStatus.NOT_FOUND

        # Admin can retrieve any job,
        # while others can only retrieve his own job
        if current_user.authority != accounts.Accounts.ADMIN_AUTHORITY \
                and result.doctor_id != current_user.get_id():
            return get_message_json('没有权限查看此任务'), HTTPStatus.FORBIDDEN

        json_res = result.to_json()
        json_res['message'] = '成功查看任务'
        return json_res, HTTPStatus.OK

    @api.doc(parser=api.parser()
             .add_argument('image_id', type=str, required=True, help='图片ID', location='form')
             .add_argument('doctor_id', type=str, required=True, help='医生ID', location='form')
             .add_argument('label_id', type=str, required=True, help='标签ID', location='form')
             .add_argument('state', type=str, required=True, help='任务状态', location='form')
             .add_argument('finished_date', type=str, required=True, help='任务完成日期', location='form')
             )
    @login_required
    def put(self, job_id):
        """Edit a single job by id."""
        # Only admin can edit any job
        if current_user.authority != accounts.Accounts.ADMIN_AUTHORITY:
            return get_message_json('没有权限编辑任务'), HTTPStatus.FORBIDDEN

        form = request.form
        try:
            result = jobs.update_job_by_id(
                job_id,
                form['image_id'],
                form['doctor_id'],
                form['label_id'],
                form['state'],
                form['finished_date']
            )
            json_res = result.to_json()
            json_res['message'] = '成功编辑任务'
            return json_res, HTTPStatus.OK
        except Exception as err:
            return handle_internal_error(str(err))

    @login_required
    def delete(self, job_id):
        """Delete a single job by id."""
        # Only admin can delete any job
        if current_user.authority != accounts.Accounts.ADMIN_AUTHORITY:
            return get_message_json('没有权限删除任务'), HTTPStatus.FORBIDDEN

        try:
            result = jobs.delete_job_by_id(job_id)
            if result == 1:
                return get_message_json('删除任务成功'), HTTPStatus.OK
            else:
                return get_message_json('删除任务失败'), HTTPStatus.BAD_REQUEST
        except Exception as err:
            return handle_internal_error(str(err))


@api.route('/')
class JobsCollectionResource(Resource):
    """Deal with collection of jobs."""

    @login_required
    def get(self):
        """List all jobs."""
        # Only admin can get all jobs
        if current_user.authority != accounts.Accounts.ADMIN_AUTHORITY:
            return get_message_json('没有权限获取所有任务'), HTTPStatus.FORBIDDEN

        try:
            result = jobs.find_all_jobs()

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

    @api.doc(parser=api.parser()
             .add_argument('image_id', type=str, required=True, help='图片ID', location='form')
             .add_argument('doctor_id', type=str, required=True, help='医生ID', location='form')
             )
    @login_required
    def post(self):
        """Create a job."""
        form = request.form
        # Only admin can create jobs
        if current_user.authority != accounts.Accounts.ADMIN_AUTHORITY:
            return get_message_json('没有权限创建任务'), HTTPStatus.FORBIDDEN
        
        try:
            result = jobs.add_job(
                form['image_id'],
                form['doctor_id']
            )
            json_res = result.to_json()
            json_res['message'] = '任务创建成功'

            return json_res, HTTPStatus.CREATED
        except Exception as err:
            return handle_internal_error(str(err))
