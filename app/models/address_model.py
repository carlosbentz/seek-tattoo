from app.configs.database import db
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from dataclasses import dataclass


@dataclass
class AddressModel(db.Model):

    id: int 
    city: str 
    state: str 
    user_id: int

    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)

    city = Column(String(50), nullable=False)
  
    state = Column(String(50), nullable=False)
    

    user_id = Column(Integer, ForeignKey('user.id'), )

    this_user = relationship('UserModel', backref='this_address')