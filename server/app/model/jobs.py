# coding=utf-8
"""Define table and operations for jobs."""
from sqlalchemy import Column, Integer, VARCHAR, DATE, ForeignKey, DATETIME, func
from . import Base, session, handle_db_exception, images, is_testing
from ..api.utils import ConstantCodes


class Jobs(Base):
    """Table constructed for jobs."""
    if is_testing:
        __tablename__ = 'TEST_Jobs'
        image_id = Column(Integer, ForeignKey('TEST_Images.image_id'))
        label_id = Column(Integer, ForeignKey('TEST_Labels.label_id'))
        account_id = Column(Integer, ForeignKey('TEST_Accounts.account_id'))
    else:
        __tablename__ = 'Jobs'
        image_id = Column(Integer, ForeignKey('Images.image_id'))
        label_id = Column(Integer, ForeignKey('Labels.label_id'))
        account_id = Column(Integer, ForeignKey('Accounts.account_id'))

    job_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    finished_date = Column(DATE)
    job_state = Column(Integer, nullable=False)

    def to_json(self):
        """Return a json for the record."""
        return {
            'job_id': self.job_id,
            'image_id': self.image_id,
            'label_id': self.label_id,
            'account_id': self.account_id,
            'finished_date': str(self.finished_date) if self.finished_date else None,
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
    job.job_state = ConstantCodes.Unlabeled
    try:
        session.add(job)
        session.commit()
        return job
    except Exception as err:
        handle_db_exception(err)


def delete_job_by_id(_job_id):
    """Delete an account by id and return 1 or 0 representing result"""
    try:
        result = session.query(Jobs).filter(Jobs.job_id == _job_id).delete()
        session.commit()
        return result
    except Exception as err:
        handle_db_exception(err)


def update_job_by_id(_job_id: int,
                     _label_id: int,
                     _finished_date: DATETIME,
                     _job_state: int,
                     the_image_id: int):
    """Update the information of a job given id and return 1 or 0 representing result"""
    try:
        result = session.query(Jobs).filter(Jobs.job_id == _job_id).update({
            'label_id': _label_id if _label_id is not None else Jobs.label_id,
            'finished_date': _finished_date if _finished_date is not None else Jobs.finished_date,
            'job_state': _job_state if _job_state is not None else Jobs.job_state
        })
        # Check whether to update corresponding image
        if _job_state == ConstantCodes.Finished:
            jobs_of_same_image = session.query(Jobs).filter(Jobs.image_id == the_image_id).all()
            images.update_image_state(the_image_id, jobs_of_same_image)
        # Regard the above operations as a transaction and ensure to commit only once
        session.commit()
        return result
    except Exception as err:
        handle_db_exception(err)


def find_job_by_id(_id: int):
    """Find a job by id and return a job object"""
    try:
        job_list = session.query(Jobs).filter(Jobs.job_id == _id)
        session.commit()
        return job_list.first()
    except Exception as err:
        handle_db_exception(err)


def find_job_by_image_id(_image_id: int):
    """Find jobs by image id and return a list"""
    try:
        job_list = session.query(Jobs).filter(Jobs.image_id == _image_id)
        session.commit()
        return job_list.all()
    except Exception as err:
        handle_db_exception(err)


def find_job_by_account_id(_account_id: int):
    """Find jobs by account id and return a list"""
    try:
        job_list = session.query(Jobs).filter(Jobs.account_id == _account_id)
        session.commit()
        return job_list.all()
    except Exception as err:
        handle_db_exception(err)


def find_job_by_label_id(_label_id: int):
    """Find jobs by label id and return a job object"""
    try:
        job_list = session.query(Jobs).filter(Jobs.label_id == _label_id)
        session.commit()
        return job_list.first()
    except Exception as err:
        handle_db_exception(err)


def find_all_jobs(_account_id: int,
                  _image_id: int,
                  _job_state: int):
    """Return all jobs related to the given arguments via a list."""
    try:
        query = {}
        if _account_id is not None:
            query['account_id'] = _account_id
        if _image_id is not None:
            query['image_id'] = _image_id
        if _job_state is not None:
            query['job_state'] = _job_state
        jobs_list = session.query(Jobs).filter_by(**query)

        session.commit()
        return jobs_list.all()
    except Exception as err:
        handle_db_exception(err)
