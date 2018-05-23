# coding=utf-8
"""Define table and operations for HRChoice."""
from sqlalchemy import Column, Integer, VARCHAR
from . import Base, session, handle_db_exception


class HRChoice(Base):
    __tablename__ = 'HRChoice'

    hr_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(VARCHAR(128), unique=True, nullable=False)

    def __repr__(self):
        return '<HRChoice: hr_id:{} name:{}>'.\
            format(self.hr_id,
                   self.name)


def add_hr_choice(_name: str):
    hr_choice = HRChoice()
    hr_choice.name = _name
    try:
        session.add(hr_choice)
        session.commit()
        return hr_choice
    except Exception as err:
        handle_db_exception(err)


def find_hr_choice_by_id(_hr_id: int):
    try:
        hr_list = session.query(HRChoice).filter(HRChoice.hr_id == _hr_id)
        session.commit()
        return  hr_list.all()
    except Exception as err:
        handle_db_exception(err)


def find_hr_choice_by_name(_name: str):
    try:
        hr_list = session.query(HRChoice).filter(HRChoice.name == _name)
        session.commit()
        return  hr_list.all()
    except Exception as err:
        handle_db_exception(err)
