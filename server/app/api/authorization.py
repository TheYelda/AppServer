# coding=utf-8
"""Deal with authorization-related APIs."""
from flask import request, current_app
from flask_restplus import Namespace, Resource
from flask_login import login_user
from werkzeug.security import check_password_hash
from ..model import accounts
from sqlalchemy.exc import IntegrityError
from .utils import get_message_json
from http import HTTPStatus


api = Namespace('authorization')


@api.route('/')
class AuthorizationResource(Resource):
    """Deal with user authorization."""

    @api.doc(parser=api.parser()
             .add_argument('username', type=str, required=True, help='username', location='form')
             .add_argument('password', type=str, required=True, help='password', location='form')
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

            login_user(account[0], True)
            return get_message_json('登录成功'), HTTPStatus.OK

        except IntegrityError as err:
            current_app.logger.exception(err.orig.args[1])
            return get_message_json('服务器内部错误'), HTTPStatus.INTERNAL_SERVER_ERROR
        except Exception as err:
            current_app.logger.exception(str(err))
            return get_message_json(str(err)), HTTPStatus.INTERNAL_SERVER_ERROR

    def delete(self):
        """Remove an authorization by token."""
        pass
