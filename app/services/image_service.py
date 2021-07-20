from flask import current_app, jsonify
from http import HTTPStatus

from app.models import ImageModel, UserModel

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

def get_images(user_id):

    # user = UserModel.query.get(user_id)

    images_of_user = ImageModel.query.get(user_id)

    return jsonify(images_of_user)
