# coding=utf-8
"""Define table and operations for HRChoice."""
from sqlalchemy import Column, Integer, VARCHAR
from . import Base


class HRChoice(Base):
    __tablename__ = 'HRChoice'

    hr_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(VARCHAR(128), unique=True, nullable=False)
