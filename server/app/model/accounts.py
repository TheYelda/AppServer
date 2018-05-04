# coding=utf-8
"""Define table and operations for accounts."""
from flask_login import UserMixin
from . import *


class Accounts(Base, UserMixin):
    """Table constructed for accounts."""
    __tablename__ = 'Accounts'

    account_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    username = Column(VARCHAR(128), nullable=False, unique=True)
    nickname = Column(VARCHAR(128), nullable=True)
    password = Column(VARCHAR(256), nullable=False)
    email = Column(VARCHAR(128), nullable=False)
    photo = Column(VARCHAR(128), nullable=True)
    authority_id = Column(Integer, ForeignKey('AuthorityChoice.authority_id'))

    def to_json(self):
        """Return a json for the record."""
        return {
            'account_id': self.account_id,
            'username': self.username,
            'nickname': self.nickname,
            'password': self.password,
            'email': self.email,
            'photo': self.photo,
            'authority_id': self.authority_id
        }

    def __repr__(self):
        return '<Accounts: account_id:{} username:{} nickname:{} password:{} email:{} photo:{} authority_id:{}>'.\
            format(self.account_id,
                   self.username,
                   self.nickname,
                   self.password,
                   self.email,
                   self.photo,
                   self.authority_id)


# def add_account(_username: str,
#                 _nickname: str,
#                 _password: str,
#                 _email: str,
#                 _photo: str):
#     """Add an account to database."""
#     account = Accounts()
#     account.username = _username
#     account.nickname = _nickname
#     account.password = _password
#     account.email = _email
#     account.photo = _photo
#     try:
#         session.add(account)
#         session.commit()
#         return account
#     except Exception as err:
#         handle_db_exception(err)


# def find_account_by_id(_account_id: int):
#     """Find an account by id and return a list"""
#     try:
#         account_list = session.query(Accounts).filter(Accounts.account_id == _account_id)
#         session.commit()
#         return account_list.all()
#     except Exception as err:
#         handle_db_exception(err)


# def find_account_by_username(_username: str):
#     """Find an account by username and return a list."""
#     try:
#         account_list = session.query(Accounts).filter(Accounts.username == _username)
#         session.commit()
#         return account_list.all()
#     except Exception as err:
#         handle_db_exception(err)


# def find_accounts_by_authority(_authority: int):
#     """Return accounts given authority via a list."""
#     try:
#         accounts_list = session.query(Accounts).filter(Accounts.authority == _authority)
#         session.commit()
#         return accounts_list.all()
#     except Exception as err:
#         handle_db_exception(err)


# def find_all_users():
#     """Return all accounts via a list."""
#     try:
#         accounts_list = session.query(Accounts).filter(Accounts.authority_id == _authority)
#         session.commit()
#         return accounts_list.all()
#     except Exception as err:
#         handle_db_exception(err)


# def update_account_by_id(_id: int,
#                          _username=None,
#                          _nickname=None,
#                          _password=None,
#                          _email=None,
#                          _photo=None,
#                          _authority=None):
#     """Update the information of an account given id and return 1 or 0 represented result"""
#     try:
#         result = session.query(Accounts).filter(Accounts.account_id == _id).update({
#             "username": _username if _username is not None else Accounts.username,
#             "nickname": _nickname if _nickname is not None else Accounts.nickname,
#             "password": _password if _password is not None else Accounts.password,
#             "email": _email if _email is not None else Accounts.email,
#             "photo": _photo if _photo is not None else Accounts.photo,
#             "authority_id": _authority if _authority is not None else Accounts.authority_id
#         })
#         session.commit()
#         return result
#     except Exception as err:
#         handle_db_exception(err)


# def delete_account_by_id(_id: int):
#     """Delete an account by id and return 1 or 0 represented result"""
#     try:
#         result = session.query(Accounts).filter(Accounts.account_id == _id).delete()
#         session.commit()
#         return result
#     except Exception as err:
#         handle_db_exception(err)
