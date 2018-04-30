# coding=utf-8
"""Define table and operations for labels."""
from . import *


class Labels(Base):
    """Table constructed for labels."""

    __tablename__ = 'Labels'

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    quality = Column(BOOLEAN, default=False)  # 图片质量
    dr = Column(BOOLEAN)  # 是否有糖尿病视网膜病变
    stage = Column(Integer)  # 所处阶段[1-7]
    dme = Column(BOOLEAN)  # 是否有糖尿病性黄斑水肿
    hr = Column(Integer)  # 高血压视网膜病变 [0-3]
    age_dme = Column(Integer)  # 年龄相关性黄斑水肿 [0-3]
    rvo = Column(BOOLEAN)  # 是否有视网膜静脉阻塞
    crao = Column(BOOLEAN)  # 是否有视网膜动脉阻塞
    myopia = Column(BOOLEAN)
    od = Column(BOOLEAN)  # 是否有病理性近视
    glaucoma = Column(BOOLEAN)  # 是否有疑似青光眼
    others = Column(BOOLEAN)  # 是否有其他疾病
    comment = Column(TEXT)  # 备注

    def to_json(self):
        """Return a json for the label."""
        return {
            'id': self.id,
            'quality': self.quality,
            'dr': self.dr,
            'stage': self.stage,
            'dme': self.dme,
            'hr': self.hr,
            'age_dme': self.age_dme,
            'rvo': self.rvo,
            'crao': self.crao,
            'myopia': self.myopia,
            'od': self.od,
            'glaucoma': self.glaucoma,
            'others': self.others,
            'comment': self.comment
        }

    def __repr__(self):
        return '<Labels: id:{}>'.format(self.id)


def add_label(_quality: BOOLEAN,
              _dr: BOOLEAN,
              _stage: int,
              _dme: BOOLEAN,
              _hr: int,
              _age_dme: int,
              _rvo: BOOLEAN,
              _crao: BOOLEAN,
              _myopia: BOOLEAN,
              _od: BOOLEAN,
              _glaucoma: BOOLEAN,
              _others: BOOLEAN,
              _comment: str):
    """Add a label to database"""
    label = Labels()
    label.quality = _quality
    label.dr = _dr
    label.stage = _stage
    label.dme = _dme
    label.hr = _hr
    label.age_dme = _age_dme
    label.rvo = _rvo
    label.crao = _crao
    label.myopia = _myopia
    label.od = _od
    label.glaucoma = _glaucoma
    label.others = _others
    try:
        session.add(label)
        session.commit()
        return  label
    except Exception as err:
        handle_db_exception(err)


def update_label_by_id(_id: int,
                       _quality: BOOLEAN,
                       _dr: BOOLEAN,
                       _stage: int,
                       _dme: BOOLEAN,
                       _hr: int,
                       _age_dme: int,
                       _rvo: BOOLEAN,
                       _crao: BOOLEAN,
                       _myopia: BOOLEAN,
                       _od: BOOLEAN,
                       _glaucoma: BOOLEAN,
                       _others: BOOLEAN,
                       _comment: str):
    """Update the information of a label given id and return 1 or 0 represented result"""
    try:
        result = session.query(Labels).filter(Labels.id == _id).update({
            "quality": _quality if _quality is not None else Labels.quality,
            "dr": _dr if _dr is not None else Labels.dr,
            "stage": _stage if _stage is not None else Labels.stage,
            "dme": _dme if _dme is not None else Labels.dme,
            "hr": _hr if _hr is not None else Labels.hr,
            "age_dme": _age_dme if _age_dme is not None else Labels.age_dme,
            "rvo": _rvo if _rvo is not None else Labels.rvo,
            "crao": _crao if _crao is not None else Labels.crao,
            "myopia": _myopia if _myopia is not None else Labels.myopia,
            "od": _od if _od is not None else Labels.od,
            "glaucoma": _glaucoma if _glaucoma is not None else Labels.glaucoma,
            "others": _others if _others is not None else Labels.others,
            "comment": _comment if _comment is not None else Labels.comment,
        })
        session.commit()
        return result
    except Exception as err:
        handle_db_exception(err)


def delete_label_by_id(_id: int):
    """Delete a label by id and return 1 or 0 represented result"""
    try:
        result = session.query(Labels).filter(Labels.id == _id).delete()
        session.commit()
        return  result
    except Exception as err:
        handle_db_exception(err)


def find_label_by_id(_id: int):
    """Return labels given id via a list"""
    try:
        label_list = session.query(Labels).filter(Labels.id == _id)
        session.commit()
        return label_list.all()
    except Exception as err:
        handle_db_exception(err)
