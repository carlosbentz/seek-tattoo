from flask import request, jsonify, current_app
from app.models.image_model import ImageModel
from http import HTTPStatus

def create(user_id):

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
    ), HTTPStatus.CREATED