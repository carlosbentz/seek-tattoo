from flask import Blueprint
from flask_jwt_extended import jwt_required
from app.services.image_service import create
from http import HTTPStatus
from app.services.image_service import delete

bp = Blueprint('bp_image', __name__, url_prefix='/user')

@bp.post('/artist/<int:user_id>/image')
@jwt_required()
def create_image(user_id: int):
    
    return create(user_id)



@bp.route('/artist/<user_id>/image/<image_id>', methods=['DELETE'])
@jwt_required()
def delete_image(user_id: int, image_id: int):

    return delete(user_id), HTTPStatus.OK

