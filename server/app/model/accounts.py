# coding=utf-8
"""Define table and operations for accounts."""
from . import *


class Accounts(Base):
    """Table constructed for accounts."""

    __tablename__ = 'Accounts'

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    username = Column(VARCHAR(128), nullable=False, unique=True)
    nickname = Column(VARCHAR(128), nullable=True)
    password = Column(VARCHAR(256), nullable=False)
    email = Column(VARCHAR(128), nullable=False)
    photo = Column(VARCHAR(128), nullable=False)
    authority = Column(Integer)

    def to_json(self):
        """Return a json for the record."""
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,  # TODO: should be password before hashing
            'email': self.email,
            'photo': self.photo,
            'authority': self.authority
        }

    def __repr__(self):
        return '<Accounts: username:{} nickname:{} password:{} email:{} photo:{} authority:{}>'.\
            format(self.username,
                   self.nickname,
                   self.password,
                   self.email,
                   self.photo,
                   self.authority)


def add_account(_username: str,
                _nickname: str,
                _password: str,
                _email: str,
                _photo: str):
    """
    :param _username: used to login
    :param _nickname: used to display
    :param _password: used to login
    :param _email: used to find password
    :param _photo: used to display
    """
    account = Accounts(username=_username,
                       nickname=_nickname,
                       password=_password,
                       email=_email,
                       photo=_photo)
    session.add(account)
    session.commit()
    return account


def find_account_by_id(_id: int,
                       find_fail_callback: func,
                       find_succeed_callback: func):
    """
    :param _id:
    :param find_fail_callback: (err)
    :param find_succeed_callback: (Account List)
    """
    try:
        account = session.query(Accounts).filter(Accounts.id == _id)
        session.commit()
        return find_succeed_callback(account.all())
    except Exception as err:
        return find_fail_callback(err)


def find_accounts_by_authority(_authority: int,
                               find_fail_callback: func,
                               find_succeed_callback: func):
    """

    :param _authority:
    :param find_fail_callback: (err)
    :param find_succeed_callback: (Account list)
    """
    try:
        accounts = session.query(Accounts).filter(Accounts.authority == _authority)
        session.commit()
        return find_succeed_callback(accounts.all())
    except Exception as err:
        return find_fail_callback(err)


def update_account_by_id(_id: int,
                         _username=None,
                         _nickname=None,
                         _password=None,
                         _email=None,
                         _photo=None,
                         _authority=None,
                         update_fail_callback=None,
                         update_succeed_callback=None):
    """
    :param _id:
    :param _username:
    :param _nickname:
    :param _password:
    :param _email:
    :param _photo:
    :param _authority:
    :param update_fail_callback: (err)
    :param update_succeed_callback: (the count of rows matched as returned by the database’s “row count” feature.)
    """
    try:
        account = session.query(Accounts).filter(Accounts.id == _id).update({
            "username": _username if _username is not None else Accounts.username,
            "nickname": _nickname if _nickname is not None else Accounts.nickname,
            "password": _password if _password is not None else Accounts.password,
            "email": _email if _email is not None else Accounts.email,
            "photo": _photo if _photo is not None else Accounts.photo,
            "_authority": _authority if _authority is not None else Accounts.authority
        })
        session.commit()
        return update_succeed_callback(account)
    except Exception as err:
        return update_fail_callback(err)


def delete_accound_by_id(_id: int,
                         delete_fail_callback=None,
                         delete_succeed_callback=None):
    """
    :param _id:
    :param delete_fail_callback: (err)
    :param delete_succeed_callback: (the count of rows matched as returned by the database’s “row count” feature.)
    """
    try:
        accounts = session.query(Accounts).filter(Accounts.id == _id).delete()
        session.commit()
        return delete_succeed_callback(accounts)
    except Exception as err:
        return delete_fail_callback(err)
