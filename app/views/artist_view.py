from flask import Blueprint,jsonify
from flask_jwt_extended import jwt_required
from app.models.user_model import UserModel


bp = Blueprint("bp_artist", __name__, url_prefix='/user')


@bp.get('/artist')
@jwt_required()
def get_artist():
    
    query = UserModel.query.filter_by(is_artist=True).all()

    return jsonify(query)