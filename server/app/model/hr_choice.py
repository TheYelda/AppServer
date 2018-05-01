# coding=utf-8
"""Define table and operations for HRChoice."""
from . import *


class HRChoice(Base):
    __tablename__ = 'HRChoice'

    hr_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(VARCHAR(128), unique=True, nullable=False)
