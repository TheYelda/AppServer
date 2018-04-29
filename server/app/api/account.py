# coding=utf-8
"""Deal with account-related APIs."""
from flask_restplus import Namespace, Resource
from werkzeug.security import generate_password_hash
from flask import request, current_app
from flask_login import login_required
from ..model import accounts
from sqlalchemy.exc import IntegrityError
from .utils import get_message_json, DB_ERR_CODES
from http import HTTPStatus

api = Namespace('accounts')


@api.route('/<int:account_id>')
class AccountResource(Resource):
    """Deal with single account."""

    @login_required
    def get(self, account_id):
        """Retrieve a single account by id."""
        try:
            result = accounts.find_account_by_id(account_id)
            if len(result) == 0:
                return get_message_json('用户ID不存在'), HTTP_CODES.NOT_FOUND
            json_res = result[0].to_json()
            json_res['message'] = '用户获取成功'
            return json_res, HTTP_CODES.OK
        except Exception as err:
            return get_message_json(str(err)), HTTP_CODES.BAD_REQUEST

    @api.doc(parser=api.parser()
             .add_argument('username', type=str, required=True, help='用户名', location='form')
             .add_argument('nickname', type=str, required=True, help='昵称', location='form')
             .add_argument('password', type=str, required=True, help='密码', location='form')
             .add_argument('email', type=str, required=True, help='邮箱', location='form')
             .add_argument('photo', type=str, required=True, help='照片文件名', location='form')
             .add_argument('authority', type=int, required=True, help='权限', location='form')
             )
    @login_required
    def put(self, account_id):
        """Edit a single account by id."""
        form = request.form
        try:
            result = accounts.update_account_by_id(
                account_id,
                form['username'],
                form['nickname'],
                form['password'],
                form['email'],
                form['photo'],
                form['authority']
            )
            if result == 1:
                json_res = form.copy()
                json_res['message'] = '修改用户信息成功'
                return json_res, HTTP_CODES.OK
            else:
                return get_message_json('修改失败'), HTTP_CODES.NOT_FOUND
        except Exception as err:
            return get_message_json(str(err)), HTTP_CODES.BAD_REQUEST

    @login_required
    def delete(self, account_id):
        """Delete a single account by id."""
        try:
            result = accounts.delete_account_by_id(account_id)
            json_res = {}
            if result == 1:
                json_res['message'] = '删除成功'
                return json_res, HTTP_CODES.DELETE
            else:
                json_res['message'] = '删除失败'
                return json_res, HTTP_CODES.NOT_FOUND
        except Exception as err:
            return get_message_json(str(err)), HTTP_CODES.BAD_REQUEST


@api.route('/')
class AccountsCollectionResource(Resource):
    """Deal with collection of accounts."""

    def get(self):
        """List all accounts."""
        pass
    
    @api.doc(parser=api.parser()
             .add_argument('username', type=str, required=True, help='用户名', location='form')
             .add_argument('nickname', type=str, required=True, help='昵称', location='form')
             .add_argument('password', type=str, required=True, help='密码', location='form')
             .add_argument('email', type=str, required=True, help='邮箱', location='form')
             .add_argument('photo', type=str, required=True, help='照片文件名', location='form')
             )
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
            json_res = result.to_json()
            # Return password before hashing
            json_res['password'] = form['password']
            json_res['message'] = '用户创建成功'

            return json_res, HTTPStatus.CREATED
        except IntegrityError as err:
            if err.orig.args[0] == DB_ERR_CODES.DUPLICATE_ENTRY:
                return get_message_json('用户名已存在'), HTTPStatus.CONFLICT
            else:
                current_app.logger.exception(err.orig.args[1])
                return get_message_json('服务器内部错误'), HTTPStatus.INTERNAL_SERVER_ERROR

        except Exception as err:
            current_app.logger.exception(str(err))
            return get_message_json('服务器内部错误'), HTTPStatus.BAD_REQUEST
