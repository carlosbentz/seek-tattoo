from flask import Blueprint,jsonify
from flask_jwt_extended import jwt_required
from app.models.user_model import UserModel
from http import HTTPStatus


bp = Blueprint("bp_artist", __name__, url_prefix='/user')


@bp.get('/artist')
@jwt_required()
def get_artist():
    
    query = UserModel.query.filter_by(is_artist=True).all()

    return jsonify(query) , HTTPStatus.OK

@bp.get('artist/<int:artist_id>')
@jwt_required()
def get_artist_id(artist_id: int):

    try:
        artist = UserModel.query.filter_by(is_artist=True, id=artist_id).first()

        if not artist:
            raise ValueError

        return jsonify(artist)
    
    except ValueError as _:
        return {"Error": "Invalid artist"}, HTTPStatus.NOT_FOUND