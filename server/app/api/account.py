# coding=utf-8
"""Deal with account-related APIs."""
from flask_restplus import Namespace, Resource
from werkzeug.security import generate_password_hash
from flask import request
from ..model import accounts
from sqlalchemy.exc import *

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

    def post(self):
        """Create an account."""
        form = request.form
        try:
            result = accounts.add_account(
                form['username'],
                form['nickname'],
                generate_password_hash(form['password']),
                form['email'],
                form['photo']
            )
            return result.to_json(), 201
        except IntegrityError as err:
            if err.orig.args[0] == 1062:
                message = '用户名已存在'
                return {'message': message}, 400
            else:
                return {'message': err.orig.args[1]}, 400
        except Exception as err:
            return {'message': str(err)}, 400
