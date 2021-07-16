from app.services.address_service import update_address
from flask import Blueprint, request, current_app, jsonify
from app.models.address_model import AddressModel
from app.exc import RequiredKeyError, MissingKeyError
from app.configs.database import db

from flask_jwt_extended import get_jwt_identity, jwt_required

from http import HTTPStatus


bp = Blueprint('bp_address', __name__, url_prefix='/user')


@bp.post("/")
@jwt_required()
def create_address():
    session =  current_app.db.session

    data = request.get_json()
    
    address = AddressModel(**data)

    session.add(address)
    session.commit()

    return jsonify(address), HTTPStatus.CREATED


@bp.route("/artist/<user_id>/address", methods=["PATCH"])
@jwt_required()
def modify_address(user_id):
    
    try:
        return update_address(user_id), HTTPStatus.OK
    
    except RequiredKeyError as e:
        return e.message

    except MissingKeyError as e:
        return e.message
