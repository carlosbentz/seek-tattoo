from flask import Blueprint, jsonify
from app.models import UserModel
from app.exc import RequiredKeyError, MissingKeyError
from app.services.user_service import delete, update

from flask_jwt_extended import get_jwt_identity, jwt_required


from http import HTTPStatus


bp = Blueprint('bp_user', __name__, url_prefix="/user")

@bp.get("/")
@jwt_required()
def get_users():
    
    users = UserModel()

    query = users.query.all()

    return jsonify({
        "users": [
            {
                "id": user.id, 
                "name": user.name, 
                "e-mail": user.email, 
                "is_artist": user.is_artist,
                "description_id": user.description_id,
            }
            for user in query
        ]
    }), HTTPStatus.OK


@bp.get("/<int:user_id>")
def get_user_by_id(user_id: int):
    users = UserModel()
    
    query = users.query.get(user_id)

    return {
        "users":
            {
                "id": query.id, 
                "name": query.name, 
                "e-mail": query.email, 
                "is_artist": query.is_artist,
                "description_id": query.description_id,

            }
    }, HTTPStatus.OK


@bp.route('/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id: int):
    print(get_jwt_identity())
    return delete(user_id), HTTPStatus.OK


@bp.route('/<int:user_id>', methods=['PATCH'])
@jwt_required()
def update_user(user_id):

    try:
        return update(user_id), HTTPStatus.OK
    
    except RequiredKeyError as e:
        return e.message

    except MissingKeyError as e:
        return e.message
