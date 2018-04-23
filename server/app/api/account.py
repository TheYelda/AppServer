# coding=utf-8
"""Deal with account-related APIs."""
from flask_restplus import Namespace, Resource, reqparse
from werkzeug.security import generate_password_hash
from flask import request
from ..model import accounts

api = Namespace('accounts')


@api.route('/<int:account_id>')
class AccountResource(Resource):
    """Deal with single account."""

    def get(self, account_id):
        """Retrieve a single account by id."""
        pass

    def put(self, account_id):
        """Edit a single account by id."""
        pass

    def delete(self, account_id):
        """Delete a single account by id."""
        pass


@api.route('/')
class AccountsCollectionResource(Resource):
    """Deal with collection of accounts."""

    def get(self):
        """List all accounts."""
        pass
    
    @api.doc(parser=api.parser().add_argument('username', type=str, required=True, help='用户名', location='form')
                                .add_argument('nickname', type=str, required=True, help='昵称', location='form')
                                .add_argument('password', type=str, required=True, help='密码', location='form')
                                .add_argument('email', type=str, required=True, help='邮箱', location='form')
                                .add_argument('photo', type=str, required=True, help='照片文件名', location='form')
    )
    def post(self):
        """Create an account."""
        form = request.form

        return accounts.add_account(
            form['username'],
            form['nickname'],
            generate_password_hash(form['password']),
            form['email'],
            form['photo'],
            lambda err: {'message': str(err.orig.args[1])},
            lambda account: account.to_json()
        )