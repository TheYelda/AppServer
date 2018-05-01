# coding=utf-8
"""Define table and operations for ImageStateChoice."""
from . import *


class ImageStateChoice(Base):
    __tablename__ = 'ImageStateChoice'

    state_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(VARCHAR(128), nullable=False, unique=True)
