from app.configs.database import db 
from sqlalchemy import Column, Integer, String
from dataclasses import dataclass



@dataclass
class ImageModel(db.Model):

    id: int
    img_url: str
    description: str

    __tablename__ = 'images'

    id = Column(Integer, primary_key=True)

    img_url = Column(String, nullable=False)

    description = Column(String)