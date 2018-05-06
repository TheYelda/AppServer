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
