# coding=utf-8
"""Deal with authorization-related APIs."""
from flask_restplus import Namespace, Resource
from .utils import get_message_json, HTTPStatus

api = Namespace('self')

@api.route('/')
class AuthorizationResource(Resource):
    """Deal with current user."""

    def get(self):
        """Retrive account_id of current user."""
        json_res = get_message_json('ID获取成功')
        json_res['account_id'] = 15
        return json_res, HTTPStatus.OK
