from app.services.address_service import update_address, create
from flask import Blueprint, request, current_app, jsonify
from app.models.address_model import AddressModel
from app.exc import RequiredKeyError, MissingKeyError
from app.configs.database import db

from flask_jwt_extended import get_jwt_identity, jwt_required

from http import HTTPStatus


bp = Blueprint('bp_address', __name__, url_prefix='/user')


@bp.post("/artist/<user_id>/address")
@jwt_required()
def create_address(user_id):
    current_user = get_jwt_identity()
    data = request.get_json()

    address = create(current_user["id"], data)


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
