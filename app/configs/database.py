from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()


def init_app(app: Flask):
    db.init_app(app)
    app.db = db

    from app.models.user_model import UserModel 
    from app.models.address_model import AddressModel
    from app.models.description_model import DescriptionModel
    from app.models.comment_model import CommentModel 
    from app.models.style_model import StyleModel
    from app.models.image_model import ImageModel
    from app.models.img_style_comments_model import ImageStyleCommentsModel
