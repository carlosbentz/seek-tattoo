from app.configs.database import db 
from sqlalchemy import Column, Integer, String
from dataclasses import dataclass


@dataclass
class StyleModel(db.Model):

    id: int 
    style_name: str 

    __tablename__ = 'styles'

    id = Column(Integer, primary_key=True)

    style_name = Column(String(50), nullable=False, unique=True)
