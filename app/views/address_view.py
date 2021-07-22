from flask import Blueprint
from app.exc import RequiredKeyError, MissingKeyError
from app.services.address_service import update_address, delete, get_by_id, get_all, create
from flask_jwt_extended import jwt_required, current_user, get_jwt_identity

from http import HTTPStatus


bp = Blueprint("address_bp", __name__, url_prefix="/user")


@bp.post("/artist/<user_id>/address")
@jwt_required()
def create_address(user_id: int):
    try:
        return create(user_id), HTTPStatus.CREATED

    except RequiredKeyError as e:
        return e.message

    except MissingKeyError as e:
        return e.message


@bp.get("/artist/<user_id>/address")
@jwt_required()
def get_address(user_id: int):
    return get_by_id(user_id), HTTPStatus.OK


@bp.get("/artist/address")
def get_all_address():
    
    return get_all(), HTTPStatus.OK


@bp.patch("/artist/<user_id>/address")
@jwt_required()
def modify_address(user_id):
    try:
        return update_address(user_id), HTTPStatus.OK
    
    except RequiredKeyError as e:
        return e.message

    except MissingKeyError as e:
        return e.message


@bp.delete("/artist/<user_id>/address")
@jwt_required()
def delete_address(user_id: int):
    
    user = get_jwt_identity()

    return delete(user_id), HTTPStatus.NO_CONTENT