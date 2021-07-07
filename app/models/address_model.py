from app.configs.database import db
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship


class AddressModel(db.Model):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)

    street = Column(String(100), nullable=False)
    number = Column(Integer, nullable=False)
    zip_code = Column(Integer, nullable=False)
    state = Column(String(50), nullable=False)
    address_active = Column(Boolean, default=True)

    user_id = Column(Integer, ForeignKey('user.id'), )

    this_user = relationship('UserModel', backref='this_address', uselist=False)