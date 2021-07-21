from flask import current_app, jsonify, request
from http import HTTPStatus

from app.models import ImageModel
from app.exc.missing_key import MissingKeyError
from app.exc.required_key import RequiredKeyError
from app.services.helper_service import verify_required_key, verify_missing_key


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


def delete(user_id: int):

    session = current_app.db.session

    found_img: ImageModel = ImageModel.query.filter_by(user_id=user_id).first()

    if not found_img:
        return {"status": "Image NOT FOUND"}, HTTPStatus.NOT_FOUND

    session.delete(found_img)
    session.commit()

    return {}


def update(img_id: int):

    session = current_app.db.session

    data = request.get_json()

    found_img: ImageModel = ImageModel.query.get(img_id)

    if not found_img:
        return {"status": "Image NOT FOUND"}, HTTPStatus.NOT_FOUND

    for key, value in data.items():
        setattr(found_img, key, value)

    session.add(found_img)
    session.commit()

    return {
        "img_url": found_img.img_url,
        "description": found_img.description,
        "user_id": found_img.user_id,
        "id": found_img.id
    }, HTTPStatus.OK


def get_images(user_id):

    images_of_user = ImageModel.query.filter_by(user_id=user_id).all()
    if not images_of_user:
        return {"status": "Image NOT FOUND"}, HTTPStatus.NOT_FOUND

    return jsonify(images_of_user)
    
def get_image_by_id(user_id):

    images_of_user = ImageModel.query.filter_by(user_id=user_id).all()
    
    if not images_of_user:
        return {"status": "Image NOT FOUND"}, HTTPStatus.NOT_FOUND

    return jsonify(images_of_user)
