# coding=utf-8
"""Deal with account-related APIs."""
from flask_restplus import Namespace, Resource

api = Namespace('accounts')


@api.route('/<int:account_id>')
class Account(Resource):
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
class AccountsCollection(Resource):
    """Deal with collection of accounts."""

    def get(self):
        """List all accounts."""
        pass

    def post(self):
        """Create an account."""
        pass
