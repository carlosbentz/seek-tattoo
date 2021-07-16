from app.models.user_model import UserModel

from app.exc.missing_key import MissingKeyError
from app.exc.required_key import RequiredKeyError

from app.services.helper_service import verify_required_key, verify_missing_key

from http import HTTPStatus
from flask import current_app, request, jsonify

def delete(user_id: int):

    session = current_app.db.session

    found_user = UserModel.query.get(user_id)

    if not found_user:
        return {"status": "User NOT FOUND"}, HTTPStatus.NOT_FOUND

    session.delete(found_user)
    session.commit()

    return {}

def update(user_id: int):

    required_keys = ["name", "email", "password_hash"]

    session = current_app.db.session

    data = request.get_json()

    if verify_missing_key(data, required_keys):
        raise MissingKeyError(data, required_keys)

    if verify_required_key(data, required_keys):
        raise RequiredKeyError(data, required_keys)

    found_user: UserModel = UserModel.query.get(user_id)

    if not found_user:
        return {"status": "User NOT FOUND"}, HTTPStatus.NOT_FOUND

    for key, value in data.items():
        setattr(found_user, key, value)

    session.add(found_user)
    session.commit()

    output =  {
        "id": found_user.id,
        "name": found_user.name,
        "email": found_user.email,
        "password_hash": found_user.password_hash,
        "is_artist": found_user.is_artist,
        "description_id": found_user.description_id,
    }

    return jsonify(output)
