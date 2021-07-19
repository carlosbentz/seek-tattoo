from app.configs.database import db 
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, backref
from dataclasses import dataclass


@dataclass 
class CommentModel(db.Model):

    id: int 
    datetime: str 
    user_id: int 
    image_id: int

    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)

    comment = Column(String, nullable=False)

    datetime = Column(Date, nullable=False)

    user_id = Column(Integer, ForeignKey('users.id'))

    image_id = Column(Integer, ForeignKey('images.id'))

    this_user = relationship('UserModel', backref=backref('this_comments', cascade="all, delete-orphan"), uselist=False)
