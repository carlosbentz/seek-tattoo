from app.configs.database import db 
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
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

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    image_id = Column(Integer, ForeignKey('images.id'), nullable=False)

    this_user = relationship('UserModel', backref='this_comments')
    


