from flask import jsonify
from app.models.user_model import UserModel


def get():

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

    return jsonify(output)


def get_by_id(artist_id):

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

    return output