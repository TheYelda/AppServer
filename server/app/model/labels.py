# coding=utf-8
"""Define table and operations for labels."""
from sqlalchemy import Column, Integer, VARCHAR, BOOLEAN, ForeignKey, TEXT, func
from . import Base, session, handle_db_exception, image_stage_choice, hr_choice, age_dme_choice
from ..api.utils import get_message_json


class Labels(Base):
    """Table constructed for labels."""

    __tablename__ = 'Labels'

    label_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    quality = Column(BOOLEAN, default=False)  # 图片质量
    dr = Column(BOOLEAN)  # 是否有糖尿病视网膜病变
    stage_id = Column(Integer, ForeignKey('ImageStageChoice.stage_id'))
    dme = Column(BOOLEAN)  # 是否有糖尿病性黄斑水肿
    hr_id = Column(Integer, ForeignKey('HRChoice.hr_id'))
    age_dme_id = Column(Integer, ForeignKey('AgeDMEChoice.agedme_id'))
    rvo = Column(BOOLEAN)  # 是否有视网膜静脉阻塞
    crao = Column(BOOLEAN)  # 受有视网膜动脉阻塞
    myopia = Column(BOOLEAN)
    od = Column(BOOLEAN)  # 是否有病理性近视
    glaucoma = Column(BOOLEAN)  # 是否有疑似青光眼
    others = Column(BOOLEAN)  # 是否有其他疾病
    comment = Column(TEXT)  # 备注

    def to_json(self):
        """Return a json for the record."""
        try:
            stage = image_stage_choice.find_image_stage_choice_by_id(self.stage_id)[0].name
            hr = hr_choice.find_hr_choice_by_id(self.hr_id)[0].name
            age_dme = age_dme_choice.find_age_dme_choice_by_id(self.age_dme_id)[0].name
            return {
                'label_id': self.label_id,
                'quality': self.quality,
                'dr': self.dr,
                'stage': stage,
                'dme': self.dme,
                'hr': hr,
                'age_dme': age_dme,
                'rvo': self.rvo,
                'crao': self.crao,
                'myopia': self.myopia,
                'od': self.od,
                'glaucoma': self.glaucoma,
                'others': self.others,
                'comment': self.comment
                }
        except Exception as err:
            handle_db_exception(str(err))

    def __repr__(self):
        return '<Labels: label_id:{} quality:{} dr:{} stage_id:{} dme:{} hr_id:{}\
                    age_dme_id:{} rvo:{} crao:{} myopia:{} od:{} glaucoma:{} others:{} comment:{}>'.\
            format(self.label_id,
                   self.quality,
                   self.dr,
                   self.stage_id,
                   self.dme,
                   self.hr_id,
                   self.age_dme_id,
                   self.rvo,
                   self.crao,
                   self.myopia,
                   self.od,
                   self.glaucoma,
                   self.others,
                   self.comment)

    def __eq__(self, other):
        if self.__class__ == other.__class__:
            for field in self.__dict__:
                if field == 'label_id' or field == 'comment' or field == '_sa_instance_state':
                    continue
                if not getattr(self, field) == getattr(other, field):
                    return False
            return True
        return False


def add_label(_quality: BOOLEAN,
              _dr: BOOLEAN,
              _stage: str,
              _dme: BOOLEAN,
              _hr: str,
              _age_dme: str,
              _rvo: BOOLEAN,
              _crao: BOOLEAN,
              _myopia: BOOLEAN,
              _od: BOOLEAN,
              _glaucoma: BOOLEAN,
              _others: BOOLEAN,
              _comment: str):
    """Add a label to database and return this label"""
    label = Labels()

    stage_list = image_stage_choice.find_image_stage_choice_by_name(_stage)
    if len(stage_list) == 0:
        result = image_stage_choice.add_image_stage_choice(_stage)
        label.stage_id = result.stage_id
    else:
        label.stage_id = stage_list[0].stage_id

    hr_list = hr_choice.find_hr_choice_by_name(_hr)
    if len(hr_list) == 0:
        result = hr_choice.add_hr_choice(_hr)
        label.hr_id = result.hr_id
    else:
        label.hr_id = hr_list[0].hr_id

    agedme_list = age_dme_choice.find_age_dme_choice_by_name(_age_dme)
    if len(agedme_list) == 0:
        result = age_dme_choice.add_age_dme_choice(_age_dme)
        label.age_dme_id = result.agedme_id
    else:
        label.age_dme_id = agedme_list[0].agedme_id

    label.quality = _quality
    label.dr = _dr
    label.dme = _dme
    label.rvo = _rvo
    label.crao = _crao
    label.myopia = _myopia
    label.od = _od
    label.glaucoma = _glaucoma
    label.others = _others
    label.comment = _comment
    try:
        session.add(label)
        session.commit()
        return label
    except Exception as err:
        handle_db_exception(err)


def update_label_by_id(_id: int,
                       _quality: BOOLEAN=None,
                       _dr: BOOLEAN=None,
                       _stage: str=None,
                       _dme: BOOLEAN=None,
                       _hr: str=None,
                       _age_dme: str=None,
                       _rvo: BOOLEAN=None,
                       _crao: BOOLEAN=None,
                       _myopia: BOOLEAN=None,
                       _od: BOOLEAN=None,
                       _glaucoma: BOOLEAN=None,
                       _others: BOOLEAN=None,
                       _comment: str=None):
    """Update the information of an label given id and return 1 or 0 represented result"""

    if _stage is not None:
        stage_list = image_stage_choice.find_image_stage_choice_by_name(_stage)
        if len(stage_list) == 0:
            result = image_stage_choice.add_image_stage_choice(_stage)
            _stage_id = result.stage_id
        else:
            _stage_id = stage_list[0].stage_id

    if _hr is not None:
        hr_list = hr_choice.find_hr_choice_by_name(_hr)
        if len(hr_list) == 0:
            result = hr_choice.add_hr_choice(_hr)
            _hr_id = result.hr_id
        else:
            _hr_id = hr_list[0].hr_id

    if _age_dme is not None:
        agedme_list = age_dme_choice.find_age_dme_choice_by_name(_age_dme)
        if len(agedme_list) == 0:
            result = age_dme_choice.add_age_dme_choice(_age_dme)
            _age_dme_id = result.agedme_id
        else:
            _age_dme_id = agedme_list[0].agedme_id

    try:
        result = session.query(Labels).filter(Labels.label_id == _id).update({
            "quality": _quality if _quality is not None else Labels.quality,
            "dr": _dr if _dr is not None else Labels.dr,
            "stage_id": _stage_id if _stage is not None else Labels.stage_id,
            "dme": _dme if _dme is not None else Labels.dme,
            "hr_id": _hr_id if _hr is not None else Labels.hr_id,
            "age_dme_id": _age_dme_id if _age_dme is not None else Labels.age_dme_id,
            "rvo": _rvo if _rvo is not None else Labels.rvo,
            "crao": _crao if _crao is not None else Labels.crao,
            "myopia": _myopia if _myopia is not None else Labels.myopia,
            "od": _od if _od is not None else Labels.od,
            "glaucoma": _glaucoma if _glaucoma is not None else Labels.glaucoma,
            "others": _others if _others is not None else Labels.others,
            "comment": _comment if _comment is not None else Labels.comment
        })
        session.commit()
        return result
    except Exception as err:
        handle_db_exception(err)


def delete_label_by_id(_id: int):
    """Delete a label by id and return 1 or 0 represented result"""
    try:
        result = session.query(Labels).filter(Labels.label_id == _id).delete()
        session.commit()
        return result
    except Exception as err:
        handle_db_exception(err)


def find_label_by_id(_id: int):
    """Find a label by id and return a label object"""
    try:
        label_list = session.query(Labels).filter(Labels.label_id == _id)
        session.commit()
        return label_list.first()
    except Exception as err:
        handle_db_exception(err)


def find_label_by_job_id(_job_id: int):
    """Find a label by job id and return a list"""
    try:
        label_list = session.query(Labels).filter(Labels.label_id == _id)
        session.commit()
        return label_list.all()
    except Exception as err:
        handle_db_exception(err)
