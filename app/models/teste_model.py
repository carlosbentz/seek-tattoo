from app.configs.database import db
from sqlalchemy import Column, Integer, String


class TesteModel(db.Model):
    __tablename__ = "teste"

    id = Column(Integer, primary_key=True)

    nome = Column(String(50))
    idade = Column(Integer)