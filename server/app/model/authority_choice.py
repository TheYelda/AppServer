# coding=utf-8
"""Define table and operations for accounts."""
from . import *


class AuthorityChoice(Base):
    __tablename__ = 'AuthorityChoice'

    authority_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(VARCHAR(128), nullable=False, unique=True)

    def __repr__(self):
        return "<AuthorityChoice: authority_id:{} name:{}>".format(self.authority_id,
                                                                   self.name)



