from app.configs.database import db 
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class ArtistModel(db.Model):
    __tablename__ = 'artist'

    id = Column(Integer, primary_key=True)

    description = Column(String)

    style_id = Column(Integer, ForeignKey('style.id'))

    this_style = relationship('StyleModel', backref='this_artist')