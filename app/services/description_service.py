from app.models import UserModel, DescriptionModel
from flask import current_app, request, jsonify


def update_description(user_id: int):
    session = current_app.db.session

    data = request.get_json()

    user = UserModel.query.get(user_id)

    if not user:
        return {"status": "User NOT FOUND"}

    found_description = DescriptionModel.query.get(user.description_id)

    for key, value in data.items():
        setattr(found_description, key, value)

    session.add(found_description)
    session.commit()

    return jsonify(found_description)



def update_description_id_in_user(user_id: int, description_id: int) -> None:
    
    session = current_app.db.session

    user = UserModel.query.get(user_id)

    if not user:
        return {"status": "User NOT FOUND"}

    user.description_id = description_id

    session.add(user)
    session.commit()


def update_is_artist(user_id) -> None:
    session = current_app.db.session

    user = UserModel.query.get(user_id)

    if user.is_artist == True:
        user.is_artist = False
    if user.is_artist == False:
        user.is_artist = True

    session.add(user)
    session.commit()


def get(user_id):
    user = UserModel.query.get(user_id)

    description = DescriptionModel.query.get(user.description_id)

    return jsonify(description)


def post(user_id):
    session =  current_app.db.session

    data = request.get_json()

    description = DescriptionModel(**data)

    session.add(description)
    session.commit()

    update_description_id_in_user(user_id, description.id)
    
    return jsonify(description)


def delete(user_id):
    session = current_app.db.session

    user = UserModel.query.get(user_id)

    update_is_artist(user_id)

    description = DescriptionModel.query.get(user.description_id)

    if not description.id == user.description_id:
        return {"error": "You're not allowed to delete other users descriptions"}

    session.delete(description)
    session.commit()

    return ""