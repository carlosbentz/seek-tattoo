from flask import Blueprint
from app import exc
from app.exc import RequiredKeyError, MissingKeyError
from app.services.description_service import post, delete, update_description, post, get
from flask_jwt_extended import jwt_required, get_jwt_identity

from http import HTTPStatus


bp = Blueprint('bp_description', __name__, url_prefix="/user")


@bp.post("/artist/<user_id>/description")
@jwt_required()
def create_description(user_id: int):
    current_user = get_jwt_identity()

    if current_user["is_artist"] == False:
        return {"status": "NOT artist"}, HTTPStatus.NOT_FOUND

    return post(user_id),  HTTPStatus.CREATED


@bp.get("/artist/<user_id>/description")
def get_description(user_id: int):
    
    return get(user_id), HTTPStatus.OK


@bp.patch("/artist/<user_id>/description")
@jwt_required()
def patch_description(user_id: int):
    try:
        return update_description(user_id), HTTPStatus.OK
    
    except RequiredKeyError as e:
        return e.message

    except MissingKeyError as e:
        return e.message


@bp.delete("/artist/<user_id>/description")
@jwt_required()
def delete_description(user_id: int):
  
    return delete(user_id), HTTPStatus.NO_CONTENT
