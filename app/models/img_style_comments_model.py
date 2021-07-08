from app.configs.database import db 
from sqlalchemy import Column, Integer, ForeignKey
from dataclasses import dataclass


@dataclass
class ImageStyleCommentsModel(db.Model):

    id: int 
    image_id: int
    style_id: int 
    user_id: int
    comment_id: int

    __tablename__ = 'image_style'

    id = Column(Integer, primary_key=True)

    image_id = Column(Integer, ForeignKey('image.id'))

    style_id = Column(Integer, ForeignKey('style.id'))

    user_id = Column(Integer, ForeignKey('user.id'))

    comment_id = Column(Integer, ForeignKey('comment.id'))
    
    