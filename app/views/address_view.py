from flask import Blueprint, request, current_app, jsonify
from app.models.address_model import AddressModel
from app.configs.database import db

from http import HTTPStatus


bp = Blueprint('bp_adress', __name__, url_prefix='/adress')


@bp.post("/")
def create_adress():
    session =  current_app.db.session

    data = request.get_json()
    
    address = AddressModel(**data)

    session.add(address)
    session.commit()

    return jsonify(address), HTTPStatus.CREATED


@bp.patch("/<user_id")
def modify_adress():
    ...
