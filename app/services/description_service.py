from app.models import UserModel, DescriptionModel
from flask import current_app, request, jsonify
from http import HTTPStatus
import ipdb


def update_description(user_id: int):
    session = current_app.db.session

    data = request.get_json()

    user = UserModel.query.get(user_id)

    description_id = user.description_id
    

    found_description = DescriptionModel.query.get(description_id)

    for key, value in data.items():
        setattr(found_description, key, value)

    session.add(found_description)
    session.commit()

    return jsonify(found_description)








def update_description_id_in_user(user_id: int, description_id: int) -> None:
    
    session = current_app.db.session

    found_user: UserModel = UserModel.query.get(user_id)

    if not found_user:
        return {"status": "User NOT FOUND"}, HTTPStatus.NOT_FOUND

    found_user.description_id = description_id

    session.add(found_user)
    session.commit()