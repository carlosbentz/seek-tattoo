from flask import Blueprint
from flask_jwt_extended import jwt_required

from http import HTTPStatus

from app.services.image_service import delete


bp = Blueprint('bp_image', __name__, url_prefix="/user")

@bp.route('/artist/<user_id>/image/<image_id>', methods=['DELETE'])
@jwt_required()
def delete_image(user_id: int, image_id: int):

    return delete(user_id), HTTPStatus.OK


bp = Blueprint('bp_image', __name__, url_prefix="/user")

@bp.route('/artist/<user_id>/image, methods=['GET'])
def get_image_by_user(user_id: int):
    
    return get(user_id), HTTPStatus.OK