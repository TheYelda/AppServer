# coding=utf-8
"""Define table and operations for jobs."""
from . import *


class Jobs(Base):
    """Table constructed for jobs."""

    __tablename__ = 'Jobs'

    job_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    image_id = Column(Integer, ForeignKey('Images.image_id'))
    doctor_id = Column(Integer, ForeignKey('Accounts.account_id'))
    state_id = Column(Integer, ForeignKey('JobStateChoice.state_id'))
    finished_date = Column(DATE)
    label_id = Column(Integer, ForeignKey('Labels.label_id'))

    def to_json(self):
        """Return a json for the record."""
        return {
            'job_id': self.image_id,
            'image_id': self.image_id,
            'doctor_id': self.label_id,
            'state_id': self.state_id,
            'finished_date': self.finished_date,
            'label_id': self.label_id
        }

    def __repr__(self):
        return '<Jobs: job_id:{} image_id:{} doctor_id:{} state_id:{} finished_date:{} label_id:{}>'.\
            format(self.job_id,
                   self.image_id,
                   self.doctor_id,
                   self.state_id,
                   self.finished_date,
                   self.label_id)


def add_job(_image_id: int,
            _doctor_id: int,
            _state_id: int,
            finished_date: DATETIME,
            label_id: int,
            add_fail_callback: func,
            add_succeed_callback: func):
    """
    :param _image_id:
    :param _doctor_id:
    :param _state:
    :param finished_date:
    :param label_id:
    :param add_fail_callback: (err)
    :param add_succeed_callback: (Jobs)
    """
    pass


def delete_job_by_id(_id,
                     find_fail_callback: func,
                     delete_fail_callback: func,
                     delete_succeed_callback: func):
    """
    :param _id:
    :param find_fail_callback:
    :param delete_fail_callback: (err)
    :param delete_succeed_callback: (None)
    """
    pass


def update_job_by_id(_id: int,
                     _image_id: int,
                     _doctor_id: int,
                     _state_id: int,
                     finished_date: DATETIME,
                     label_id: int,
                     find_fail_callback: func,
                     update_fail_callback: func,
                     update_succeed_callback: func):
    """
    :param _id:
    :param _image_id:
    :param _doctor_id:
    :param _state:
    :param finished_date:
    :param label_id:
    :param find_fail_callback: (err)
    :param update_fail_callback: (err)
    :param update_succeed_callback: (Jobs)
    """
    pass


def find_job_by_id(_id: int,
                   find_fail_callback: func,
                   find_succeed_callback: func):
    """
    :param _id:
    :param find_fail_callback: (err)
    :param find_succeed_callback: (Jobs)
    """
    pass


def find_jobs_by_state(_state_id: int,
                       find_fail_callback: func,
                       find_succeed_callback: func):
    """
    :param _state_id:
    :param find_fail_callback: (err)
    :param find_succeed_callback: (Jobs List)
    """
    pass
