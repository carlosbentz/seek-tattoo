from app.configs.database import db 
from sqlalchemy import Column, Integer, String, ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash

class UserModel(db.Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)

    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password_hash = Column(String)

    artist_id = Column(Integer, ForeignKey('artist.id'), unique=True)

    @property
    def password(self):
        raise AttributeError("Password cannot be accessed!")

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

  
    def verify_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)