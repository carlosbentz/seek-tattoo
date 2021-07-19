from flask import Blueprint, current_app, jsonify, request
from app.models import AddressModel
from app.exc import RequiredKeyError, MissingKeyError
from app.configs.database import db
from app.services.address_service import update_address, delete, get, get_all
from flask_jwt_extended import jwt_required

from http import HTTPStatus


bp = Blueprint('bp_address', __name__, url_prefix='/user')


@bp.post("/artist/<user_id>/address")
# @jwt_required()
def create_address(user_id: int):
    
    session =  current_app.db.session

    data = request.get_json()

    address = AddressModel(**data)

    address.user_id = user_id

    session.add(address)
    session.commit()

    return jsonify(address)
    
    # try:
    #     return create(user_id), HTTPStatus.CREATED

    # except RequiredKeyError as e:
    #     return e.message

    # except MissingKeyError as e:
    #     return e.message


@bp.get("/artist/address")
def get_all_address():
    
    return get_all(), HTTPStatus.OK


@bp.get("/artist/<user_id>/address")
@jwt_required
def get_address(user_id: int):

    return get(user_id), HTTPStatus.OK


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
@jwt_required
def delete_address(user_id: int):

    return delete(user_id), HTTPStatus.NO_CONTENT