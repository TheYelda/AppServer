# coding=utf-8
"""Define table and operations for ImageStateChoice."""
from . import *


class ImageStageChoice(Base):
    __tablename__ = 'ImageStageChoice'

    stage_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(VARCHAR(128), nullable=False, unique=True)

    def to_json(self):
        return{
            'stage_id': self.stage_id,
            'name': self.name
        }

    def __repr__(self):
        return '<ImageStageChoice: stage_id:{} name:{}>'.\
            format(self.stage_id,
                   self.name)


def add_image_stage_choice(_name: str):
    imageStateChoice = ImageStageChoice()
    imageStateChoice.name = _name
    try:
        session.add(imageStateChoice)
        session.commit()
        return imageStateChoice
    except Exception as err:
        handle_db_exception(err)


def find_image_stage_choice_by_id(_stage_id: int):
    try:
        stage_list = session.query(ImageStageChoice).filter(ImageStageChoice.stage_id == _stage_id)
        session.commit()
        return stage_list.all()
    except Exception as err:
        handle_db_exception(err)


def find_image_stage_choice_by_name(_name: str):
    try:
        stage_list = session.query(ImageStageChoice).filter(ImageStageChoice.name == _name)
        session.commit()
        return  stage_list.all()
    except Exception as err:
        handle_db_exception(err)
