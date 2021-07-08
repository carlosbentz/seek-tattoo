from app.configs.database import db 
from sqlalchemy import Column, Integer, String


class StyleModel(db.Model):
    __tablename__ = 'style'

    id = Column(Integer, primary_key=True)

    style_name = Column(String, nullable=False, unique=True)