from flask import Blueprint,jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.user_model import UserModel
from http import HTTPStatus


bp = Blueprint("bp_artist", __name__, url_prefix='/user')


@bp.get('/artist')
@jwt_required()
def get_artist():
    
    query = UserModel.query.filter_by(is_artist=True).all()
    output = [ 
        {
            "User": {
                "id": art.id,
                "name": art.name,
                "email": art.email,
                "is_artist": art.is_artist,
                "description_id": art.description_id,
                "address": f"/user/artist/{art.id}/address",
                "description": f"user/artist/{art.id}/description",
                "images": f"user/artist/{art.id}/image"
            }
        }

        for art in query
        ]

    return jsonify(output) , HTTPStatus.OK

@bp.get('artist/<int:artist_id>')
@jwt_required()
def get_artist_id(artist_id: int):

    try:
        artist = UserModel.query.filter_by(is_artist=True, id=artist_id).first()

        if artist:

            output = {
                "User": {
                    "id": artist.id,
                    "name": artist.name,
                    "email": artist.email,
                    "is_artist": artist.is_artist,
                    "description_id": artist.description_id,
                    "address": f"/user/artist/{artist.id}/address",
                    "description": f"user/artist/{artist.id}/description",
                    "images": f"user/artist/{artist.id}/image"
                }
            }


        if not artist:
            raise ValueError

        return jsonify(output), HTTPStatus.OK
    
    except ValueError as _:
        return {"Error": "Invalid artist"}, HTTPStatus.NOT_FOUND