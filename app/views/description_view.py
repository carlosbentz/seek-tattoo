from flask import Blueprint, request, jsonify, current_app
from app import exc
from app.models import UserModel, DescriptionModel, AddressModel
from app.exc import RequiredKeyError, MissingKeyError
from app.services.user_service import delete, update, update_description
from flask_jwt_extended import create_access_token


from http import HTTPStatus


bp = Blueprint('bp_description', __name__, url_prefix="/user")

# POST description - precisa ter um user_id na URL

@bp.post("/artist/<user_id>/description")
def create_artist(user_id: int):

    session =  current_app.db.session
    data = request.get_json()

    description = DescriptionModel(**data)

    session.add(description)
    session.commit()

    update_description(user_id, description.id)

    return jsonify(description),  HTTPStatus.CREATED


# GET todos os cadastros de artistas

@bp.get("/artist")
def get_all_artist():
    users = UserModel()
    description = DescriptionModel()
    address = AddressModel()

    user = users.query.filter_by(is_artist=True)

    return {
        "users": [
            {
                "id": user.id, 
                "name": user.name, 
                "e-mail": user.email, 
                "is_artist": user.is_artist,
                "description_id": user.description_id,
            }
            
        ]
    }, HTTPStatus.OK
    
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

# GET de um artista pelo user_id

# PATCH dos dados da tabela descrption

# DELETE deleta o cadastro de artista e muda na tabela user is_artist=FALSE