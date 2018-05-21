# coding=utf-8
"""Define table and operations for AgeDMEChoice."""
from sqlalchemy import Column, Integer, VARCHAR
from . import Base, session, handle_db_exception


class AgeDMEChoice(Base):
    __tablename__ = 'AgeDMEChoice'

    agedme_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(VARCHAR(128), nullable=False, unique=True)

    def __repr__(self):
        return '<AgeDMEChoice: hr_id:{} name:{}>'.\
            format(self.agedme_id,
                   self.name)


def add_age_dme_choice(_name: str):
    agedme_choice = AgeDMEChoice()
    agedme_choice.name = _name
    try:
        session.add(agedme_choice)
        session.commit()
        return agedme_choice
    except Exception as err:
        handle_db_exception(err)


def find_age_dme_choice_by_id(_agedme_id: int):
    try:
        agedme_list = session.query(AgeDMEChoice).filter(AgeDMEChoice.agedme_id == _agedme_id)
        session.commit()
        return  agedme_list.all()
    except Exception as err:
        handle_db_exception(err)


def find_age_dme_choice_by_name(_name: str):
    try:
        agedme_list = session.query(AgeDMEChoice).filter(AgeDMEChoice.name == _name)
        session.commit()
        return  agedme_list.all()
    except Exception as err:
        handle_db_exception(err)