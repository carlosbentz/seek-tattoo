from app.configs.database import db 
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from dataclasses import dataclass



@dataclass
class ImageModel(db.Model):

    id: int
    img_url: str
    description: str
    user_id: int

    __tablename__ = 'images'

    id = Column(Integer, primary_key=True)

    img_url = Column(String, nullable=False, unique=True)

    description = Column(String(200), nullable=False)

    user_id = Column(Integer, ForeignKey('users.id'))

    this_style = relationship('StyleModel', cascade="all, delete", backref='this_images', secondary="image_styles", uselist=False)

    this_comment = relationship('CommentModel', cascade="all, delete-orphan", backref=backref('this_image', uselist=False))
