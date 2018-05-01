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
        return '<Accounts: username:{} nickname:{} password:{} email:{} photo:{} authority_id:{}>'.\
            format(self.username,
                   self.nickname,
                   self.password,
                   self.email,
                   self.photo,
                   self.authority_id)


def add_account(_username: str,
                _nickname: str,
                _password: str,
                _email: str,
                _photo: str):
    """Add an account to databse."""
    account = Accounts()
    account.username = _username
    account.nickname = _nickname
    account.password = _password
    account.email = _email
    account.photo = _photo
    try:
        session.add(account)
        session.commit()
        return account
    except Exception as err:
        handle_db_exception(err)


def find_account_by_id(_id: int):
    """Find an account by id."""
    try:
        account = session.query(Accounts).filter(Accounts.account_id == _id)
        session.commit()
        return account.all()
    except Exception as err:
        handle_db_exception(err)


def find_account_by_username(_username: str):
    """Find an account by username."""
    try:
        account = session.query(Accounts).filter(Accounts.username == _username)
        session.commit()
        return account.all()
    except Exception as err:
        handle_db_exception(err)


def find_accounts_by_authority(_authority: int):
    """Return accounts given authority."""
    try:
        accounts = session.query(Accounts).filter(Accounts.authority_id == _authority)
        session.commit()
        return accounts.all()
    except Exception as err:
        handle_db_exception(err)


def update_account_by_id(_id: int,
                         _username=None,
                         _nickname=None,
                         _password=None,
                         _email=None,
                         _photo=None,
                         _authority=None):
    """Update the information of an account given id."""
    try:
        account = session.query(Accounts).filter(Accounts.account_id == _id).update({
            "username": _username if _username is not None else Accounts.username,
            "nickname": _nickname if _nickname is not None else Accounts.nickname,
            "password": _password if _password is not None else Accounts.password,
            "email": _email if _email is not None else Accounts.email,
            "photo": _photo if _photo is not None else Accounts.photo,
            "authority_id": _authority if _authority is not None else Accounts.authority_id
        })
        session.commit()
        return account
    except Exception as err:
        handle_db_exception(err)


def delete_account_by_id(_id: int):
    """Delete an account by id."""
    try:
        accounts = session.query(Accounts).filter(Accounts.account_id == _id).delete()
        session.commit()
        return accounts
    except Exception as err:
        handle_db_exception(err)
