# coding=utf-8
"""Deal with account-related APIs."""
from flask_restplus import Namespace, Resource
from werkzeug.security import generate_password_hash
from flask import request
from flask_login import login_required, current_user
from sqlalchemy.exc import IntegrityError
from ..model import accounts
from .utils import get_message_json, DB_ERR_CODES, handle_internal_error, HTTPStatus, ConstCodes


api = Namespace('accounts')


@api.route('/<int:account_id>')
class AccountResource(Resource):
    """Deal with single account."""

    @login_required
    def get(self, account_id):
        """Retrieve a single account by id."""
        try:
            if not current_user.is_admin():
                if current_user.account_id != account_id:
                    return get_message_json('只有管理员能访问他人账号'), HTTPStatus.UNAUTHORIZED
            result = accounts.find_account_by_id(account_id)
            if len(result) == 0:
                return get_message_json('用户ID不存在'), HTTPStatus.NOT_FOUND
            json_res = result[0].to_json()
            json_res['message'] = '用户获取成功'
            return json_res, HTTPStatus.OK
        except Exception as err:
            return handle_internal_error(str(err))

    @api.doc(parser=api.parser()
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
            """doctor and guest can not modify their authority or other users' info"""
            """admin can not modify his authority"""
            """admin can not modify other users' authority as admin"""
            if not current_user.is_admin():
                if account_id == current_user.account_id and int(form['authority']) != current_user.authority:
                    return get_message_json('用户权限不足以修改自己的权限等级'), HTTPStatus.UNAUTHORIZED
                elif account_id != current_user.account_id:
                    return get_message_json('用户权限不足以修改他人信息'), HTTPStatus.UNAUTHORIZED
            elif current_user.is_admin() and account_id == current_user.account_id \
                    and int(form['authority']) != ConstCodes.Admin:
                return get_message_json('不能修改管理员自己的权限'), HTTPStatus.UNAUTHORIZED
            elif current_user.is_admin() and account_id != current_user.account_id \
                    and int(form['authority']) == ConstCodes.Admin:
                return get_message_json('管理员不能将他人权限改为管理员'), HTTPStatus.UNAUTHORIZED
            result = accounts.update_account_by_id(
                account_id,
                form['nickname'],
                generate_password_hash(form['password']),
                form['email'],
                form['photo'],
                form['authority']
            )
            if result == 1:
                json_res = form.copy()
                json_res['message'] = '修改用户信息成功'
                return json_res, HTTPStatus.OK
            else:
                return get_message_json('修改失败，用户ID不存在'), HTTPStatus.NOT_FOUND
        except Exception as err:
            return handle_internal_error(str(err))

    @login_required
    def delete(self, account_id):
        """Delete a single account by id."""
        try:
            if not current_user.is_admin() and current_user.account_id != account_id:
                return get_message_json('用户权限不足以删除他人账户'), HTTPStatus.UNAUTHORIZED
            elif current_user.is_admin() and current_user.account_id == account_id:
                return get_message_json('不能删除管理员账户'), HTTPStatus.UNAUTHORIZED
            result = accounts.delete_account_by_id(account_id)
            if result == 1:
                return get_message_json('删除成功'), HTTPStatus.NO_CONTENT
            else:
                return get_message_json('删除失败，用户ID不存在'), HTTPStatus.NOT_FOUND
        except Exception as err:
            return handle_internal_error(err)


@api.route('/')
class AccountsCollectionResource(Resource):
    """Deal with collection of accounts."""

    @login_required
    def get(self):
        """List all accounts."""
        try:
            if not current_user.is_admin():
                return get_message_json('用户权限不足以查看所有账户'), HTTPStatus.UNAUTHORIZED
            result = accounts.find_all_users()
            accounts_list = []
            for i, account in enumerate(result):
                accounts_list.append(account.to_json())
            json_res = {'message': '查找成功',
                        'data': accounts_list}
            return json_res, HTTPStatus.OK
        except Exception as err:
            return get_message_json(str(err))
    
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
                return handle_internal_error(err.orig.args[1])

        except Exception as err:
            return handle_internal_error(str(err))
