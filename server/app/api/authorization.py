# coding=utf-8
"""Deal with authorization-related APIs."""
from sqlalchemy.exc import IntegrityError
from flask import request, current_app
from flask_restplus import Namespace, Resource
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash
from ..model import accounts
from .utils import get_message_json, handle_internal_error, HTTPStatus

api = Namespace('authorization')

@api.route('/')
class AuthorizationResource(Resource):
    """Deal with user authorization."""

    @api.doc(parser=api.parser()
             .add_argument('username', type=str, required=True, help='用户名', location='form')
             .add_argument('password', type=str, required=True, help='密码', location='form')
            )
    def post(self):
        """Create authorization given username and password."""
        return get_message_json('登录成功'), HTTPStatus.CREATED

    def delete(self):
        """Remove an authorization by token."""
        return get_message_json('登出成功'), HTTPStatus.NO_CONTENT
