# coding=utf-8
"""Define table and operations for images."""
from sqlalchemy import Column, Integer, VARCHAR, ForeignKey
from . import Base, session, handle_db_exception


class Images(Base):
    """Table constructed for images."""

    __tablename__ = 'Images'

    image_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    image_state = Column(Integer, nullable=False)
    filepath = Column(VARCHAR(128), nullable=False)
    source = Column(VARCHAR(128))

    def to_json(self):
        """Return a json for the record."""
        return {
            'image_id': self.image_id,
            'image_state': self.image_state,
            'filepath': self.filepath,
            'source': self.source
        }
    
    def __repr__(self):
        return '<Images: image_id:{} image_state:{} filepath:{}, source{}>'.\
            format(self.image_id, self.image_state, self.filepath, self.source)


def add_image(_image_state: int,
              _filepath: str,
              _source: str):

    return []


def update_image_by_id(_id: int,
                       _filename=None,
                       _state_id=None,
                       _label_id=None,
                       _source=None):
    """
    :param _id:
    :param _filename:
    :param _state:
    :param _ground_truth_id:
    :param _source:
    :return:
    """
    return []


def find_image_by_id(_id: int):
    """
    :param _id:
    :param find_fail_callback: (err)
    :param find_succeed_callback: (Image)
    :return:
    """
    return []


def find_images_by_state(_state: int):
    """
    :param _state:
    :return:
    """
    return []


def delete_image_by_id(_id: int):
    """
    :param _id:
    :return:
    """
    return []
