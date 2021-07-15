from app.configs.database import db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from dataclasses import dataclass


@dataclass
class AddressModel(db.Model):

    id: int 
    city: str 
    state: str 
    user_id: int

    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)

    city = Column(String(100), nullable=False)
  
    state = Column(String(2), nullable=False)
    
    user_id = Column(Integer, ForeignKey('users.id'))

    this_user = relationship('UserModel', cascade="all, delete", backref='this_address')
