# coding=utf-8
"""Deal with authorization-related APIs."""
from sqlalchemy.exc import IntegrityError
from flask import request
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
        req_password = request.form['password']
        try:
            account = accounts.find_account_by_username(request.form['username'])
            if not account or len(account) == 0:
                return get_message_json('用户不存在'), HTTPStatus.BAD_REQUEST

            if not check_password_hash(account[0].password, req_password):
                return get_message_json('密码错误'), HTTPStatus.BAD_REQUEST

            login_user(account[0], remember=True)
            return get_message_json('登录成功'), HTTPStatus.OK

        except IntegrityError as err:
            handle_internal_error(err.orig.args[1])
        except Exception as err:
            handle_internal_error(str(err))

    @login_required
    def delete(self):
        """Remove an authorization by token."""
        logout_user()
        return get_message_json('登出成功'), HTTPStatus.OK
