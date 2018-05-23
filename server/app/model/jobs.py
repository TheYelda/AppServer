# coding=utf-8
"""Define table and operations for jobs."""
from sqlalchemy import Column, Integer, VARCHAR, DATE, ForeignKey, DATETIME, func
from . import Base, session, handle_db_exception
from ..api.utils import ConstCodes


class Jobs(Base):
    """Table constructed for jobs."""

    __tablename__ = 'Jobs'

    job_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    image_id = Column(Integer, ForeignKey('Images.image_id'))
    label_id = Column(Integer, ForeignKey('Labels.label_id'))
    account_id = Column(Integer, ForeignKey('Accounts.account_id'))
    finished_date = Column(DATE)
    job_state = Column(Integer, nullable=False)

    def to_json(self):
        """Return a json for the record."""
        return {
            'job_id': self.image_id,
            'image_id': self.image_id,
            'label_id': self.label_id,
            'account_id': self.account_id,
            'finished_date': self.finished_date,
            'job_state': self.job_state
        }

    def __repr__(self):
        return '<Jobs: job_id:{} image_id:{} label_id:{} account_id:{} finished_date:{} job_state:{}>'.\
            format(self.job_id,
                   self.image_id,
                   self.label_id,
                   self.account_id,
                   self.finished_date,
                   self.job_state)


def add_job(_image_id: int,
            _account_id: int):
    """Add a job to database."""
    job = Jobs()
    job.image_id = _image_id
    job.account_id = _account_id
    job.job_state = ConstCodes.Unlabeled
    try:
        session.add(job)
        session.commit()
        return job
    except Exception as err:
        handle_db_exception(err)


def delete_job_by_id(_id):
    """Delete an account by id and return 1 or 0 representing result"""
    try:
        result = session.query(Jobs).filter(Jobs.account_id == _id).delete()
        session.commit()
        return result
    except Exception as err:
        handle_db_exception(err)


def update_job_by_id(_id: int,
                     _image_id: int,
                     _account_id: int,
                     _label_id: int,
                     _finished_date: DATETIME,
                     _job_state: int):
    """Update the information of a job given id and return 1 or 0 representing result"""
    try:
        result = session.query(Jobs).filter(Jobs.account_id == _id).update({
            'job_id': _id,
            'image_id': _image_id,
            'label_id': _label_id,
            'account_id': _account_id,
            'finished_date': _finished_date,
            'job_state': _job_state
        })
        session.commit()
        return result
    except Exception as err:
        handle_db_exception(err)


def find_job_by_id(_id: int):
    """Find an account by id and return a list"""
    try:
        job_list = session.query(Jobs).filter(Jobs.job_id == _id)
        session.commit()
        return job_list.all()
    except Exception as err:
        handle_db_exception(err)


def find_all_jobs(_account_id):
    """Return all jobs or jobs related to the given account id via a list."""
    try:
        if _account_id is None:
            jobs_list = session.query(Jobs).filter()
        else:
            jobs_list = session.query(Jobs).filter(Jobs.account_id == _account_id)

        session.commit()
        return jobs_list.all()
    except Exception as err:
        handle_db_exception(err)
