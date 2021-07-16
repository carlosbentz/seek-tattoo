from flask import Blueprint, jsonify
from app.models.user_model import UserModel
from flask_jwt_extended import jwt_required


bp = Blueprint('bp_client', __name__, url_prefix='/user')


@bp.get('/client')
@jwt_required()
def get_client():

    query = UserModel.query.filter_by(is_artist=False).all()

    return jsonify(query)