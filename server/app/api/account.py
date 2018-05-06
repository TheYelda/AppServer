# coding=utf-8
"""Deal with account-related APIs."""
from flask_restplus import Namespace, Resource
from werkzeug.security import generate_password_hash
from flask import request
from flask_login import login_required, current_user
from sqlalchemy.exc import IntegrityError
from ..model import accounts
from .utils import get_message_json, DB_ERR_CODES, handle_internal_error, HTTPStatus

api = Namespace('accounts')

""" ---------- These are for Testing ----------- """
SINGLE_ACCOUNT_RESPONSE = {
    'account_id': 33,
    'username': 'doctora',
    'nickname': 'kevin',
    'email': 'abc@gg.com',
    'photo': 'a.png',
    'authority': 1
}
COLLECTION_ACCOUNT_RESPONSE = {
    'message': '',
    'data':
        [
            {
                'account_id': 33,
                'username': 'doctora',
                'nickname': 'kevin',
                'email': 'abc@gg.com',
                'photo': 'a.png',
                'authority_id': 1
            },{
                'account_id': 308,
                'username': 'doctorb',
                'nickname': 'bbbb',
                'email': 'bbb@gg.com',
                'photo': 'b.png',
                'authority_id': 2
            },{
                'account_id': 2446,
                'username': 'doctorc',
                'nickname': 'cc',
                'email': 'c@gg.com',
                'photo': 'c.png',
                'authority_id': 1
            }
        ]
}
""" -------------------------------------------- """

@api.route('/<int:account_id>')
class AccountResource(Resource):
    """Deal with single account."""

    def get(self, account_id):
        """Retrieve a single account by id."""
        SINGLE_ACCOUNT_RESPONSE['message'] = '账户获取成功'
        return SINGLE_ACCOUNT_RESPONSE, HTTPStatus.OK

    @api.doc(parser=api.parser()
             .add_argument('username', type=str, required=True, help='用户名', location='form')
             .add_argument('nickname', type=str, required=True, help='昵称', location='form')
             .add_argument('password', type=str, required=True, help='密码', location='form')
             .add_argument('email', type=str, required=True, help='邮箱', location='form')
             .add_argument('photo', type=str, required=True, help='照片文件名', location='form')
             .add_argument('authority', type=int, required=True, help='权限', location='form')
             )
    def put(self, account_id):
        """Edit a single account by id."""
        SINGLE_ACCOUNT_RESPONSE['message'] = '账户编辑成功'
        return SINGLE_ACCOUNT_RESPONSE, HTTPStatus.OK

    def delete(self, account_id):
        """Delete a single account by id."""
        return get_message_json('账户删除成功'), HTTPStatus.NO_CONTENT


@api.route('/')
class AccountsCollectionResource(Resource):
    """Deal with collection of accounts."""

    def get(self):
        """List all accounts."""
        COLLECTION_ACCOUNT_RESPONSE['message'] = '账户集合获取成功'
        return COLLECTION_ACCOUNT_RESPONSE, HTTPStatus.OK
    
    @api.doc(parser=api.parser()
             .add_argument('username', type=str, required=True, help='用户名', location='form')
             .add_argument('nickname', type=str, required=True, help='昵称', location='form')
             .add_argument('password', type=str, required=True, help='密码', location='form')
             .add_argument('email', type=str, required=True, help='邮箱', location='form')
             .add_argument('photo', type=str, required=True, help='照片文件名', location='form')
             )
    def post(self):
        """Create an account."""
        SINGLE_ACCOUNT_RESPONSE['message'] = '账户创建成功'
        return SINGLE_ACCOUNT_RESPONSE, HTTPStatus.CREATED
