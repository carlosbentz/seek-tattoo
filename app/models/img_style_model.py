from app.configs.database import db 
from sqlalchemy import Column, Integer, ForeignKey
from dataclasses import dataclass


@dataclass
class ImageStyleModel(db.Model):

    id: int 
    image_id: int
    style_id: int 

    __tablename__ = 'image_styles'

    id = Column(Integer, primary_key=True)

    image_id = Column(Integer, ForeignKey('images.id'))

    style_id = Column(Integer, ForeignKey('styles.id'))
