from flask import Blueprint
from http import HTTPStatus
from app.services.artist_service import get, get_by_id


bp = Blueprint("bp_artist", __name__, url_prefix='/user')


@bp.get('/artist')
def get_artist():
    
    artists = get()

    return artists , HTTPStatus.OK

@bp.get('artist/<int:artist_id>')
def get_artist_id(artist_id: int):

    try:
        return get_by_id(artist_id), HTTPStatus.OK
    
    except ValueError as _:
        return {"Error": "Invalid artist"}, HTTPStatus.NOT_FOUND
