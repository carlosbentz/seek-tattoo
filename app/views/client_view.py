from flask import Blueprint, jsonify
from app.models.user_model import UserModel
from flask_jwt_extended import jwt_required
from http import HTTPStatus


bp = Blueprint('bp_client', __name__, url_prefix='/user')


@bp.get('/client')
@jwt_required()
def get_client():

    query = UserModel.query.filter_by(is_artist=False).all()

    return jsonify(query), HTTPStatus.OK

@bp.get('/client/<int:client_id>')
@jwt_required()
def get_client_id(client_id):

    try: 
        client = UserModel.query.filter_by(is_artist=False, id=client_id).first()

        if not client:
            raise ValueError 
        
        return jsonify(client), HTTPStatus.OK
    
    except ValueError as _:
        return {"Error": "Invalid client"}, HTTPStatus.NOT_FOUND
