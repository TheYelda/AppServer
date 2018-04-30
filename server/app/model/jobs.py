# coding=utf-8
"""Define table and operations for jobs."""
from . import *


class Jobs(Base):
    """Table constructed for jobs."""

    __tablename__ = 'Jobs'

    # states
    UNLABELED = 0
    LABELING = 1
    FINISHED = 2

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    image_id = Column(Integer, ForeignKey('Images.id'))
    doctor_id = Column(Integer, ForeignKey('Accounts.id'))
    state = Column(Integer)
    finished_date = Column(DATE)
    label_id = Column(Integer, ForeignKey('Labels.id'))

    def to_json(self):
        """Return a json for the record."""
        return {
            'id': self.id,
            'image_id': self.image_id,
            'doctor_id': self.doctor_id,
            'state': self.state,
            'finished_date': self.finished_date,
            'label_id': self.label_id
        }

    def __repr__(self):
        return '<Jobs: image_id:{} doctor_id:{} state:{} finished_date:{} label_id:{}>'.\
            format(self.image_id,
                   self.doctor_id,
                   self.state,
                   self.finished_date,
                   self.label_id)


test = []


def add_job(_image_id: int,
            _doctor_id: int):
    """
    Add a new job.
    :return: the new-created job object
    """
    job = Jobs()
    job.image_id = _image_id
    job.doctor_id = _doctor_id
    job.state = Jobs.UNLABELED

    # Test
    import copy
    temp = copy.copy(job)
    temp.id = 1
    test.append(temp)
    return temp

    # TODO
    try:
        session.add(job)
        session.commit()
        return job
    except Exception as err:
        handle_db_exception(err)


def delete_job_by_id(_id):
    """
    Delete a job by id.
    :param _id: job id
    :return: 1 or 0, standing for success or failure
    """
    # Test
    for job in test:
        if job.id == _id:
            test.remove(job)
            return 1
    return 0


def update_job_by_id(_id: int,
                     _image_id: int,
                     _doctor_id: int,
                     _label_id: int,
                     _state: int,
                     _finished_date: Date):
    """
    Update job by id.
    :return: the updated job object
    """
    # Test
    for job in test:
        if job.id == _id:
            job.image_id = _image_id
            job.doctor_id = _doctor_id
            job.label_id = _label_id
            job.state = _state
            job.finished_date = _finished_date
            return job


def find_job_by_id(_id: int):
    """
    Find job by id.
    :return: list of 0 or 1 jobs
    """
    # Test
    res = []
    for job in test:
        if job.id == _id:
            res.append(job)
    return res


def find_all_jobs():
    """
    Get all jobs.
    :return: list of all jobs
    """
    # Test
    return test
