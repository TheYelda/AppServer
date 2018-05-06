# coding=utf-8
"""Define table and operations for images."""
from . import *


class Images(Base):
    """Table constructed for images."""

    __tablename__ = 'Images'

    image_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    label_id = Column(Integer, ForeignKey('Labels.label_id'))
    state_id = Column(Integer, ForeignKey('ImageStateChoice.state_id'))
    filename = Column(VARCHAR(128), nullable=False)
    Source = Column(VARCHAR(128))

    def to_json(self):
        """Return a json for the record."""
        return {
            'image_id': self.image_id,
            'label_id': self.label_id,
            'state_id': self.state_id,
            'filename': self.filename,
            'Source': self.Source
        }
    
    def __repr__(self):
        return '<Images: image_id:{} label_id:{} state_id:{} filename:{}, Source{}>'.\
            format(self.image_id, self.label_id, self.state_id, self.filename, self.Source)
