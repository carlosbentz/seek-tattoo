from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from http import HTTPStatus

from app.models.image_model import ImageModel
from app.exc import RequiredKeyError, MissingKeyError
from app.services.image_service import delete, update

bp = Blueprint('bp_image', __name__, url_prefix="/user")

@bp.route('/artist/<user_id>/image/<image_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id: int):

    return delete(user_id), HTTPStatus.OK


@bp.patch('/artist/<user_id>/image/<image_id>', methods=["PATCH"])
def update(user_id: int, image_id: int):
    
    try:
        return update(image_id), HTTPStatus.OK
    
    except RequiredKeyError as e:
        return e.message

    except MissingKeyError as e:
        return e.message

    