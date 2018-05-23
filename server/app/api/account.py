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
                    return get_message_json('用户无法访问他人账号'), HTTPStatus.UNAUTHORIZED
            result = accounts.find_account_by_id(account_id)
            if len(result) == 0:
                return get_message_json('用户不存在'), HTTPStatus.NOT_FOUND
            json_res = result[0].to_json()
            json_res['message'] = '用户获取成功'
            return json_res, HTTPStatus.OK
        except Exception as err:
            return handle_internal_error(str(err))

    @login_required
    @api.doc(parser=api.parser()
             .add_argument('body', type=str, required=True, help='json', location='json')
            )
    def put(self, account_id):
        """Edit a single account by id."""
        form = request.get_json()
        try:
            """doctor and guest can not modify their authority or other users' info"""
            """admin can not modify his authority"""
            """admin can not modify other users' authority as admin"""
            if not current_user.is_admin():
                if account_id == current_user.account_id and int(form['authority']) != current_user.authority:
                    return get_message_json('用户无法修改权限'), HTTPStatus.UNAUTHORIZED
                elif account_id != current_user.account_id:
                    return get_message_json('用户无法修改他人信息'), HTTPStatus.UNAUTHORIZED
            elif current_user.is_admin() and account_id == current_user.account_id \
                    and int(form['authority']) != ConstCodes.Admin:
                return get_message_json('管理员无法修改本账号权限'), HTTPStatus.UNAUTHORIZED
            elif current_user.is_admin() and account_id != current_user.account_id \
                    and int(form['authority']) == ConstCodes.Admin:
                return get_message_json('管理员无法修改他人权限为管理员'), HTTPStatus.UNAUTHORIZED
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
                json_res['message'] = '用户修改成功'
                return json_res, HTTPStatus.OK
            else:
                return get_message_json('用户不存在'), HTTPStatus.NOT_FOUND
        except Exception as err:
            return handle_internal_error(str(err))

    @login_required
    def delete(self, account_id):
        """Delete a single account by id."""
        try:
            if not current_user.is_admin() and current_user.account_id != account_id:
                return get_message_json('用户无法删除他人账号'), HTTPStatus.UNAUTHORIZED
            elif current_user.is_admin() and current_user.account_id == account_id:
                return get_message_json('管理员不可删除'), HTTPStatus.UNAUTHORIZED
            result = accounts.delete_account_by_id(account_id)
            if result == 1:
                return get_message_json('用户删除成功'), HTTPStatus.NO_CONTENT
            else:
                return get_message_json('用户不存在'), HTTPStatus.NOT_FOUND
        except Exception as err:
            return handle_internal_error(str(err))


@api.route('/')
class AccountsCollectionResource(Resource):
    """Deal with collection of accounts."""

    @login_required
    @api.doc(parser=api.parser()
             .add_argument('username', type=str, required=False, help='username', location='args')
            )
    def get(self):
        """List all accounts."""
        try:
            query_username = request.args.get('username')
            if not current_user.is_admin():
                return get_message_json('用户无法查看他人账号'), HTTPStatus.UNAUTHORIZED
            result = accounts.find_all_users()
            accounts_list = []
            if query_username:
                for _, account in enumerate(result):
                    if account.username == query_username:
                        accounts_list.append(account.to_json())
            else:
                for _, account in enumerate(result):
                    accounts_list.append(account.to_json())

            json_res = {'message': '用户集合获取成功',
                        'data': accounts_list}
            return json_res, HTTPStatus.OK
        except Exception as err:
            return get_message_json(str(err))
    
    @api.doc(parser=api.parser()
             .add_argument('body', type=str, required=True, help='json', location='json')
            )
    def post(self):
        """Create an account."""
        form = request.get_json()

        try:
            result = accounts.add_account(
                form['username'],
                form['nickname'],
                generate_password_hash(form['password']),
                form['email'],
                'default.png'
            )
            json_res = result.to_json()
            json_res['message'] = '用户创建成功'

            return json_res, HTTPStatus.CREATED
        except IntegrityError as err:
            if err.orig.args[0] == DB_ERR_CODES.DUPLICATE_ENTRY:
                return get_message_json('用户名已存在'), HTTPStatus.CONFLICT
            else:
                return handle_internal_error(err.orig.args[1])

        except Exception as err:
            return handle_internal_error(str(err))
