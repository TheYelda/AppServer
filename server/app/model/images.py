# coding=utf-8
"""Define table and operations for images."""
from . import *


class Images(Base):
    """Table constructed for images."""

    __tablename__ = 'Images'

<<<<<<< HEAD
    image_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    label_id = Column(Integer, ForeignKey('Labels.label_id'))
    state_id = Column(Integer, ForeignKey('ImageStateChoice.state_id'))
=======
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    state = Column(Integer)
>>>>>>> 77a0c67f556d32e3a8fdd3f4ed67002411cd72af
    filename = Column(VARCHAR(128), nullable=False)
    Source = Column(VARCHAR(128))

    def to_json(self):
        """Return a json for the record."""
        return {
            'id': self.image_id,
            'ground_truth_id': self.label_id,
            'state': self.state_id,
            'filename': self.filename,
            'Source': self.Source
        }
    
    def __repr__(self):
        return '<Images: ground_truth_id:{} state:{} source:{}>'.\
            format(self.label_id, self.state_id, self.Source)


def add_image(_filename: str,
              _state_id: int,
              _source: str):
    """
    :param _state_id:
    :param _filename:
    :param _source:
    """
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
