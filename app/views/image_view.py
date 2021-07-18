from flask import Blueprint, request, jsonify, current_app
from app.models.image_model import ImageModel
from flask_jwt_extended import jwt_required
from http import HTTPStatus

bp = Blueprint('bp_image', __name__, url_prefix='/user')

@bp.post('/artist/<int:user_id>/image')
@jwt_required()
def create_image(user_id: int):
    
    session = current_app.db.session 

    data = request.get_json()

    image = ImageModel(**data)

    image.user_id = user_id

    session.add(image)
    session.commit()

    return jsonify(
        {
            "Image": image
        }
    )

    ...