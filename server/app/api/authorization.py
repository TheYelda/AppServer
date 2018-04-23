# coding=utf-8
"""Deal with authorization-related APIs."""
from flask import request
from flask_restplus import Namespace, Resource, reqparse
from flask_login import login_user
from werkzeug.security import check_password_hash, generate_password_hash
from ..model.accounts import find_account_by_username

api = Namespace('authorization')

def fail_callback(err):
    print(err)
    return []

def succeed_callback(accounts):
    return accounts

@api.route('/')
class AuthorizationResource(Resource):
    """Deal with user authorization."""

    @api.doc(parser=api.parser().add_argument('username', type=str, required=True, help='username', location='form')
                                .add_argument('password', type=str, required=True, help='password', location='form')
    )
    def post(self):
        """Create authorization given username and password."""

        req_username = request.form['username']
        req_password = request.form['password']
        account = find_account_by_username(req_username, fail_callback, succeed_callback)

        if len(account) == 0:
            return {'message': '用户不存在'}, 400
        
        if not check_password_hash(account[0].password, req_password):
            return {'message': '密码错误'}, 400

        login_user(account[0], True)

    def delete(self):
        """Remove an authorization by token."""
        pass
