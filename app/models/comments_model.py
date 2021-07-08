from app.configs.database import db 
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship


class CommentsModel(db.Model):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)

    datetime = Column(DateTime, nullable=False)

    user_id = Column(Integer, ForeignKey('user.id'))

    this_user = relationship('UserModel', backref='this_comments')

    artist_id = Column(Integer, ForeignKey('artist.id'))

    this_artist = relationship('ArtistModel', backref='this_comments')


