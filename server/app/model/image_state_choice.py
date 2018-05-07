# coding=utf-8
"""Define table and operations for ImageStateChoice."""
from . import *


class ImageStageChoice(Base):
    __tablename__ = 'ImageStageChoice'

    stage_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(VARCHAR(128), nullable=False, unique=True)
