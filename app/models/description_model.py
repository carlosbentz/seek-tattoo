from app.configs.database import db 
from sqlalchemy import Column, Integer, String
from dataclasses import dataclass


@dataclass
class DescriptionModel(db.Model):

    id: int 
    experience: int
    trait: str 
    paint: str
    description: str
    studio_name: str

    __tablename__ = 'descriptions'

    id = Column(Integer, primary_key=True)

    experience = Column(Integer, nullable=False)

    trait = Column(String(50), nullable=False)

    paint = Column(String(100), nullable=False)

    studio_name = Column(String(100))

    description = Column(String)
