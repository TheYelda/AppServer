# coding=utf-8
"""Define table and operations for images."""
from sqlalchemy import Column, Integer, VARCHAR, ForeignKey
from . import Base, session, handle_db_exception, labels
from ..api.utils import ConstantCodes


class Images(Base):
    """Table constructed for images."""

    __tablename__ = 'Images'

    image_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    label_id = Column(Integer, ForeignKey('Labels.label_id'), nullable=True)
    image_state = Column(Integer, nullable=False)
    filename = Column(VARCHAR(128), nullable=False, unique=True)
    source = Column(VARCHAR(128))

    def to_json(self):
        """Return a json for the record."""
        return {
            'image_id': self.image_id,
            'label_id':self.label_id,
            'image_state': self.image_state,
            'filename': self.filename,
            'source': self.source
        }
    
    def __repr__(self):
        return '<Images: image_id:{} label_id{} image_state:{} filename:{}, source{}>'.\
            format(self.image_id, self.label_id, self.image_state, self.filename, self.source)


def add_image(_image_state: int,
              _filename: str,
              _source: str):
    image = Images()
    image.image_state = _image_state
    image.filename = _filename
    image.source = _source
    try:
        session.add(image)
        session.commit()
        return image
    except Exception as err:
        handle_db_exception(err)


def update_image_by_id(_id: int,
                       _label_id=None,
                       _image_state=None,
                       _filename=None,
                       _source=None):
    try:
        result = session.query(Images).filter(Images.image_id == _id).update({
            "label_id": _label_id if _label_id is not None else Images.label_id,
            "image_state": _image_state if _image_state is not None else Images.image_state,
            "filename": _filename if _filename is not None else Images.filename,
            "source": _source if _source is not None else Images.source
        })
        session.commit()
        return result
    except Exception as err:
        handle_db_exception(err)


def find_image_by_id(_id: int):
    try:
        image_list = session.query(Images).filter(Images.image_id == _id)
        session.commit()
        return image_list.first()
    except Exception as err:
        handle_db_exception(err)


def find_image_by_label_id(_label_id: int):
    try:
        image_list = session.query(Images).filter(Images.label_id == _label_id)
        session.commit()
        return image_list.first()
    except Exception as err:
        handle_db_exception(err)


def find_all_images(_state):
    try:
        if _state is None:
            image_list = session.query(Images).filter()
        else:
            _state = int(_state)
            image_list = session.query(Images).filter(Images.image_state == _state)

        session.commit()
        return image_list.all()
    except Exception as err:
        handle_db_exception(err)


def delete_image_by_id(_id: int):
    try:
        result = session.query(Images).filter(Images.image_id == _id).delete()
        session.commit()
        return result
    except Exception as err:
        handle_db_exception(err)


def update_image_state(_image_id, all_jobs):
    """
    Update the state of the image relative to the given jobs
    :param _image_id: the id of the to-be-updated image
    :param all_jobs: all corresponding jobs of the image
    """
    # Only when all jobs are finished will we move on
    for job in all_jobs:
        if job.job_state != ConstantCodes.Finished:
            return
    # Check if all corresponding labels are consistant
    all_labels = [labels.find_label_by_id(job.label_id) for job in all_jobs]
    if all_labels.count(all_labels[0]) == len(all_labels):
        update_image_by_id(_image_id, _label_id=all_labels[0].label_id, _image_state=ConstantCodes.Done)
    else:
        update_image_by_id(_image_id, _image_state=ConstantCodes.Different)
