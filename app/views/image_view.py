from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.services.image_service import create
from http import HTTPStatus

from app.exc import RequiredKeyError, MissingKeyError

from app.services.image_service import delete, update
from app.services.image_service import delete, get_images, get_image_by_id, get_all_images, create_image_style, get_styles

bp = Blueprint('bp_image', __name__, url_prefix='/user')


@bp.post('/artist/<int:user_id>/image')
@jwt_required()
def create_image(user_id: int):
    
    return create(user_id)


@bp.delete('/artist/<user_id>/image/<image_id>')
@jwt_required()
def delete_image(user_id: int, image_id: int):

    return delete(user_id), HTTPStatus.OK


@bp.get('/artist/<user_id>/image')
def get_image_by_user(user_id: int):
    
    return get_images(user_id), HTTPStatus.OK


@bp.patch('/artist/<user_id>/image/<image_id>')
@jwt_required()
def update_image(user_id: int, image_id: int):
    
    try:
        return update(image_id), HTTPStatus.OK
    
    except RequiredKeyError as e:
        return e.message

    except MissingKeyError as e:
        return e.message

    
@bp.get('/artist/<user_id>/image/<image_id>')
def get_image_by_id_of_artist(user_id: int, image_id):
    res  = get_image_by_id(image_id)

    if not res:
        return {"status": "Image NOT FOUND"}, HTTPStatus.NOT_FOUND

    
    return res, HTTPStatus.OK


@bp.get('/artist/image')
def get_all_artist_images():
    images = get_all_images()

    page = request.args.get('page', type=int) or 1
    per_page = request.args.get('per_page', type=int) or len(images) + 1
    actual_page = page * per_page
    previous_page = (page -1) * per_page

    if per_page > len(images):
        return jsonify(images)

    return jsonify([image for i, image in enumerate(images) if i >= previous_page and i < actual_page])


    # return get_all_images(), HTTPStatus.OK


@bp.post("/artist/<user_id>/image/<image_id>/style")
@jwt_required()
def post_image_style(user_id, image_id):
    data = request.get_json()

    return create_image_style(image_id, data["style_id"])


@bp.get('/artist/image/style')
def get_all_styles():

    return get_styles()