from app.configs.database import db 
from sqlalchemy import Column, Integer, String


class ImageModel(db.Model):
    __tablename__ = 'image'

    id = Column(Integer, primary_key=True)

    img_url = Column(String, nullable=False)