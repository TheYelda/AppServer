# coding=utf-8
"""Define table and operations for JobStateChoice."""
from . import *


class JobStateChoice(Base):
    __tablename__ = 'JobStateChoice'

    state_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(VARCHAR(128), unique=True, nullable=False)

