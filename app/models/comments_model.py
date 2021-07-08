from app.configs.database import db 
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from dataclasses import dataclass


@dataclass 
class CommentsModel(db.Model):

    id: int 
    datatime: str 
    user_id: int 

    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)

    comment = Column(String, nullable=False)

    datetime = Column(DateTime, nullable=False)

    user_id = Column(Integer, ForeignKey('user.id'))

    this_user = relationship('UserModel', backref='this_comments', secondary='ImageStyleCommentsModel')



