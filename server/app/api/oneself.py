# coding=utf-8
"""Deal with onself-related APIs."""
from flask_restplus import Namespace, Resource
from flask_login import login_required, current_user
from .utils import handle_internal_error, HTTPStatus

api = Namespace('myself')


@api.route('/')
class MyselfResource(Resource):
    """deal with myself"""

    @login_required
    def get(self):
        """Retrieve a id for myself"""
        try:
            json_res = {'message': 'ID获取成功',
                        'accound_id': current_user.id}
            return json_res, HTTPStatus.OK
        except Exception as err:
            return handle_internal_error(str(err))

