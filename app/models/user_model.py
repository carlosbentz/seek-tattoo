from app.configs.database import db 
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
from dataclasses import dataclass


@dataclass
class UserModel(db.Model):

    id: int
    name: str
    email: str 
    is_artist: bool
    description_id: int 

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)

    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password_hash = Column(String)

    is_artist = Column(Boolean, default=False)

    description_id = Column(Integer, ForeignKey('descriptions.id'))

    this_description = relationship('DescriptionModel', backref='this_user', uselist=False)

    @property
    def password(self):
        raise AttributeError("Password cannot be accessed!")

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

  
    def verify_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)