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
            'authority': self.authority
        }

    def __repr__(self):
        return '<Accounts: account_id:{} username:{} nickname:{} password:{} email:{} photo:{} authority_id:{}>'.\
            format(self.account_id,
                   self.username,
                   self.nickname,
                   self.password,
                   self.email,
                   self.photo,
                   self.authority)
