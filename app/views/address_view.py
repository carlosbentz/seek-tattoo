from app.services.address_view import update_address
from flask import Blueprint, request, current_app, jsonify
from app.models.address_model import AddressModel
from app.exc import RequiredKeyError, MissingKeyError
from app.configs.database import db

from http import HTTPStatus


bp = Blueprint('bp_address', __name__, url_prefix='/address')


@bp.post("/")
def create_adress():
    session =  current_app.db.session

    data = request.get_json()
    
    address = AddressModel(**data)

    session.add(address)
    session.commit()

    return jsonify(address), HTTPStatus.CREATED


@bp.route("/<int:address_id>", methods=["PATCH"])
def modify_adress(address_id):
    
    try:
        return update_address(address_id), HTTPStatus.OK
    
    except RequiredKeyError as e:
        return e.message

    except MissingKeyError as e:
        return e.message
