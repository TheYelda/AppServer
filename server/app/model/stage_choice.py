# coding=utf-8
"""Define table and operations for StageChoice."""
from . import *


class StageChoice(Base):
    __tablename__ = 'StageChoice'

    stage_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(VARCHAR(128), unique=True, nullable=False)
