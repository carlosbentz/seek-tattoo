from flask import Blueprint, jsonify
from app.models.user_model import UserModel
from app.models.description_model import DescriptionModel
from app import exc

from app.exc import RequiredKeyError, MissingKeyError
from app.services.user_service import delete, update

from http import HTTPStatus

bp = Blueprint('bp_user_artist', __name__, url_prefix="/user")

@bp.get("/artist")
def find_all_artist():
    users = UserModel()

    query = users.query


    ...

"""
    {
    "Users": [
        "User": {
            "name": <name>: str,
            "email": <email>: str,
            "is_artist": True: Boolean,
            "description_id": <description_id>: int,
            "id": <id>: int,
            "address": "/user/artist/<user_id>/address",
            "description": "user/artist/<user_id>/description",
            "images": "user/artist/<user_id>/image"
        },
    ]
}

HTTP Status: 200 OK
"""

@bp.get("/artist/<int:user_id>")
def find_artist_by_id(user_id: int):
    
    ...


"""
    {
    "User": {
        "name": <name>: str,
        "email": <email>: str,
        "is_artist": True: Boolean,
        "description_id": <description_id>: int,
        "id": <id>: int,
        "address": "/user/artist/<user_id>/address",
        "description": "user/artist/<user_id>/description",
        "images": "user/artist/<user_id>/image"
    }
}

HTTP Status: 200 OK
"""