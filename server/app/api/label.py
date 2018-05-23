# coding=utf-8
"""Deal with label-related APIs."""
from flask_restplus import Namespace, Resource, reqparse
from flask_login import login_required,current_user
from flask import request
from ..model import labels, jobs
from .utils import get_message_json, handle_internal_error, HTTPStatus

api = Namespace('labels')


@api.route('/<int:label_id>')
class LabelResource(Resource):
    """Deal with single label."""

    @login_required
    def get(self, label_id):
        """Retrieve a single label by id."""
        try:
            if not current_user.is_admin():
                # TODO
                '    and current_user.account_id != jobs.find_accound_id_by_lable_id(label_id):'
                return get_message_json('用户无法访问其他用户的标注信息'), HTTPStatus.UNAUTHORIZED
            result = labels.find_label_by_id(label_id)
            if len(result) == 0:
                return get_message_json('标注不存在'), HTTPStatus.NOT_FOUND
            json_res = result[0].to_json()
            json_res['message'] = '标注获取成功'
            return json_res, HTTPStatus.OK
        except Exception as err:
            return handle_internal_error(str(err))

    @login_required
    @api.doc(parser=api.parser()
             .add_argument('body', type=str, required=True, help='json', location='json')
             )
    def put(self, label_id):
        """Edit a single label by id."""
        form = request.get_json()
        try:
            result = labels.update_label_by_id(
                label_id,
                form['quality'],
                form['dr'],
                form['stage'],
                form['dme'],
                form['hr'],
                form['age_dme'],
                form['rvo'],
                form['crao'],
                form['myopia'],
                form['od'],
                form['glaucoma'],
                form['others'],
                form['comment']
            )
            if result == 1:
                json_res = form.copy()
                json_res['message'] = '标注修改成功'
                return json_res, HTTPStatus.OK
            else:
                return get_message_json('标注不存在'), HTTPStatus.NOT_FOUND
        except Exception as err:
            return handle_internal_error(str(err))

    @login_required
    def delete(self, label_id):
        """Delete a single label by id."""
        try:
            result = labels.delete_label_by_id(label_id)
            if result == 1:
                return get_message_json('标注删除成功'), HTTPStatus.OK
            else:
                return get_message_json('标注不存在'), HTTPStatus.NOT_FOUND
        except Exception as err:
            return handle_internal_error(str(err))


@api.route('/')
class LabelsCollectionResource(Resource):
    """Deal with collection of labels."""

    @login_required
    @api.doc(parser=api.parser()
             .add_argument('body', type=str, required=True, help='json', location='json')
             )
    def post(self):
        """Create a label."""
        form = request.get_json()
        try:
            result = labels.add_label(
                form['quality'],
                form['dr'],
                form['stage'],
                form['dme'],
                form['hr'],
                form['age_dme'],
                form['rvo'],
                form['crao'],
                form['myopia'],
                form['od'],
                form['glaucoma'],
                form['others'],
                form['comment'])
            json_res = result.to_json()
            json_res['message'] = '标注创建成功'
            return json_res, HTTPStatus.CREATED
        except Exception as err:
            return handle_internal_error(str(err))
