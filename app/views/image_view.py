from flask import Blueprint
from flask_jwt_extended import jwt_required

from http import HTTPStatus

from app.services.image_service import delete, get_images, get_image_by_id


bp = Blueprint('bp_image', __name__, url_prefix="/user")

@bp.route('/artist/<user_id>/image/<image_id>', methods=['DELETE'])
@jwt_required()
def delete_image(user_id: int, image_id: int):

    return delete(user_id), HTTPStatus.OK


@bp.route('/artist/<user_id>/image', methods=['GET'])
def get_image_by_user(user_id: int):
    
    return get_images(user_id), HTTPStatus.OK


@bp.route('/artist/<user_id>/image/<image_id>', methods=['GET'])
def get_image_by_id_of_artist(user_id: int, image_id):
    
    return get_image_by_id(user_id), HTTPStatus.OK