from app.configs.database import db 
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from dataclasses import dataclass


@dataclass
class StyleModel(db.Model):

    id: int 
    style_name: str 
    user_id: int 

    __tablename__ = 'style'

    id = Column(Integer, primary_key=True)

    style_name = Column(String, nullable=False, unique=True)

    user_id = Column(Integer, ForeignKey('user.id'))

    this_user = relationship('UserModel', backref='this_style', secondary='ImageStyleCommentsModel')
