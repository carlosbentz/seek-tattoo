from flask import Blueprint
from app.models import UserModel
from app.exc import RequiredKeyError, MissingKeyError
from app.services.user_service import delete, update

from http import HTTPStatus


bp = Blueprint('bp_user', __name__, url_prefix="/user")

@bp.get("/")
def get_users():
    
    users = UserModel()

    query = users.query.all()

    return {
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
    }, HTTPStatus.OK


@bp.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id: int):

    return delete(user_id), HTTPStatus.OK


@bp.route('/user/<int:user_id>', methods=['PATCH'])
def update_user(user_id):

    try:
        return update(user_id), HTTPStatus.OK
    
    except RequiredKeyError as e:
        return e.message

    except MissingKeyError as e:
        return e.message
