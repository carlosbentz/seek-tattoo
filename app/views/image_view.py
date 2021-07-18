from flask import Blueprint
from flask_jwt_extended import jwt_required
from app.services.image_service import create

bp = Blueprint('bp_image', __name__, url_prefix='/user')

@bp.post('/artist/<int:user_id>/image')
@jwt_required()
def create_image(user_id: int):
    
    return create(user_id)