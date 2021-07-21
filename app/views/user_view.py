from flask import Blueprint, jsonify
from app.models import UserModel
from app.exc import RequiredKeyError, MissingKeyError
from app.services.user_service import delete, update, get, get_by_id

from flask_jwt_extended import jwt_required


from http import HTTPStatus


bp = Blueprint('bp_user', __name__, url_prefix="/user")

@bp.get("/")
@jwt_required()
def get_users():
    users = get()

    return users, HTTPStatus.OK


@bp.get("/<int:user_id>")
def get_user_by_id(user_id: int):
    user = get_by_id(user_id)
    
    return user, HTTPStatus.OK


@bp.delete('/<int:user_id>')
@jwt_required()
def delete_user(user_id: int):

    return delete(user_id), HTTPStatus.OK


@bp.patch('/<int:user_id>')
@jwt_required()
def update_user(user_id):

    try:
        return update(user_id), HTTPStatus.OK
    
    except RequiredKeyError as e:
        return e.message

    except MissingKeyError as e:
        return e.message
