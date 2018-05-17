# coding=utf-8
"""Define table and operations for labels."""
from sqlalchemy import Column, Integer, VARCHAR, BOOLEAN, ForeignKey, TEXT, func
from . import Base, session, handle_db_exception


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
    od = Column(BOOLEAN)  # 是否有病理性近视
    glaucoma = Column(BOOLEAN)  # 是否有疑似青光眼
    others = Column(BOOLEAN)  # 是否有其他疾病
    comment = Column(TEXT)  # 备注

    def to_json(self):
        """Return a json for the record."""
        return {
            'label_id': self.label_id,
            'quality': self.quality,
            'dr': self.dr,
            'stage_id': self.stage_id,
            'dme': self.dme,
            'hr_id': self.hr_id,
            'age_dme_id': self.age_dme_id,
            'rvo': self.rvo,
            'crao': self.crao,
            'od': self.od,
            'glaucoma': self.glaucoma,
            'others': self.others,
            'comment': self.comment
            }

    def __repr__(self):
        return '<Jobs: label_id:{} quality:{} dr:{} stage_id:{} stage_id:{} dme:{} hr_id:{}\
                    age_dme_id:{} rvo:{} crao:{} od:{} glaucoma:{} others:{} comment:{}>'.\
            format(self.label_id,
                   self.quality,
                   self.dr,
                   self.stage_id,
                   self.dme,
                   self.hr_id,
                   self.age_dme_id,
                   self.rvo,
                   self.crao,
                   self.od,
                   self.glaucoma,
                   self.others,
                   self.comment)


def add_label(_quality: BOOLEAN,
              _dr: BOOLEAN,
              _stage: int,
              _dme: BOOLEAN,
              _hr: int,
              _age_dme: int,
              _rvo: BOOLEAN,
              _crao: BOOLEAN,
              _od: BOOLEAN,
              _glaucoma: BOOLEAN,
              _others: BOOLEAN,
              _comment: str,
              add_fail_callback: func,
              add_succeed_callback: func):
    pass


def update_label_by_id(_id: int,
                       _quality: BOOLEAN,
                       _dr: BOOLEAN,
                       _stage: int,
                       _dme: BOOLEAN,
                       _hr: int,
                       _age_dme: int,
                       _rvo: BOOLEAN,
                       _crao: BOOLEAN,
                       _od: BOOLEAN,
                       _glaucoma: BOOLEAN,
                       _others: BOOLEAN,
                       _comment: str,
                       find_fail_callback: func,
                       update_fail_callback: func):
    pass


def delete_label_by_id(_id: int,
                       find_fail_callback: func,
                       delete_fail_callback: func,
                       delete_succeed_callback: func):
    pass


def find_label_by_id(_id: int,
                     find_fail_callback: func,
                     find_succeed_callback: func):
    pass
