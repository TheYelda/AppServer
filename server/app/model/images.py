# coding=utf-8
"""Define table and operations for images."""
from . import *


class Images(Base):
    """Table constructed for images."""

    __tablename__ = 'Images'

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    ground_truth_id = Column(Integer, ForeignKey('GroundTruthLabels.id'))
    state = Column(Integer)
    filename = Column(VARCHAR(128), nullable=False)
    Source = Column(VARCHAR(128))

    def to_json(self):
        """Return a json for the record."""
        return {
            'id': self.id,
            'ground_truth_id': self.ground_truth_id,
            'state': self.state,
            'filename': self.filename,
            'Source': self.Source
        }
    
    def __repr__(self):
        return '<Images: ground_truth_id:{} state:{} info_id:{}>'.\
            format(self.ground_truth_id, self.state, self.info_id)


def add_image(_filename: str,
              _state: str,
              _source: str):
    """
    :param _state:
    :param _filename:
    :param _source:
    """
    return []


def update_image_by_id(_id: int,
                       _filename=None,
                       _state=None,
                       _ground_truth_id=None,
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
