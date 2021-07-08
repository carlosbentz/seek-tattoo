from app.configs.database import db 
from sqlalchemy import Column, Integer, String
from dataclasses import dataclass


@dataclass
class DescriptionModel(db.Model):

    id: int 
    trait: str 
    paints: str  

    __tablename__ = 'description'

    id = Column(Integer, primary_key=True)

    experience = Column(String, nullable=False)

    trait = Column(String(50), nullable=False)

    paints = Column(String(100), nullable=False)