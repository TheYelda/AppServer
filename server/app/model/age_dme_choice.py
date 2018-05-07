# coding=utf-8
"""Define table and operations for AgeDMEChoice."""
from . import *


class AgeDMEChoice(Base):
    __tablename__ = 'AgeDMEChoice'

    agedme_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(VARCHAR(128), nullable=False, unique=True)