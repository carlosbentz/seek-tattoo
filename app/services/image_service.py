from flask import current_app, request, jsonify
from http import HTTPStatus

from app.models import ImageModel

from app.exc.missing_key import MissingKeyError
from app.exc.required_key import RequiredKeyError

from app.services.helper_service import verify_required_key, verify_missing_key


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


