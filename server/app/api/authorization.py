# coding=utf-8
"""Deal with authorization-related APIs."""
from flask import request
from flask_restplus import Namespace, Resource, reqparse
from flask_login import login_user
from werkzeug.security import check_password_hash, generate_password_hash
from ..model import accounts

api = Namespace('authorization')

@api.route('/')
class AuthorizationResource(Resource):
    """Deal with user authorization."""

    @api.doc(parser=api.parser().add_argument('username', type=str, required=True, help='username', location='form')
                                .add_argument('password', type=str, required=True, help='password', location='form')
    )
    def post(self):
        """Create authorization given username and password."""

        req_password = request.form['password']
        account = accounts.find_account_by_username(
            request.form['username'],
            lambda err: print(err),
            lambda accounts: accounts)

        if not account or len(account) == 0:
            return {'message': '用户不存在'}, 400
        
        if not check_password_hash(account[0].password, req_password):
            return {'message': '密码错误'}, 400

        login_user(account[0], True)
        return {'message': '登录成功'}, 200


    def delete(self):
        """Remove an authorization by token."""
        pass
