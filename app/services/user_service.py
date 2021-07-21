from app.models.user_model import UserModel

from app.exc.missing_key import MissingKeyError
from app.exc.required_key import RequiredKeyError

from app.services.helper_service import verify_required_key, verify_missing_key

from http import HTTPStatus
from flask import current_app, request, jsonify

from flask_jwt_extended import create_access_token

def delete(user_id: int):

    session = current_app.db.session

    found_user = UserModel.query.get(user_id)

    if not found_user:
        return {"status": "User NOT FOUND"}, HTTPStatus.NOT_FOUND

    session.delete(found_user)
    session.commit()

    return {}

def update(user_id: int):

    required_keys = ["name", "email", "password"]

    session = current_app.db.session

    data = request.get_json()

    if verify_required_key(data, required_keys):
        raise RequiredKeyError(data, required_keys)

    if verify_missing_key(data, required_keys):
        raise MissingKeyError(data, required_keys)

    found_user: UserModel = UserModel.query.get(user_id)

    if not found_user:
        return {"status": "User NOT FOUND"}, HTTPStatus.NOT_FOUND

    for key, value in data.items():
        setattr(found_user, key, value)

    session.add(found_user)
    session.commit()

    output =  {
        "User": {
            "name": found_user.name,
            "email": found_user.email,
            "is_artist": found_user.is_artist,
            "description_id": found_user.description_id,
        }
    }

    return jsonify(output)


def get():
    users = UserModel()

    query = users.query.all()

    return jsonify({
        "users": [
            {
                "id": user.id, 
                "name": user.name, 
                "e-mail": user.email, 
                "is_artist": user.is_artist,
                "description_id": user.description_id,
            }
            for user in query
        ]
    })


def get_by_id(user_id):
    users = UserModel()
    
    query = users.query.get(user_id)

    return {
        "users":
            {
                "id": query.id, 
                "name": query.name, 
                "e-mail": query.email, 
                "is_artist": query.is_artist,
                "description_id": query.description_id,

            }
    }
def signup():

    required_keys = ["name", "email", "password", "is_artist"]

    session =  current_app.db.session

    data = request.get_json()

    if verify_missing_key(data, required_keys):
        raise MissingKeyError(data, required_keys)

    if verify_required_key(data, required_keys):
        raise RequiredKeyError(data, required_keys)

    password_to_hash = data.pop('password')

    user = UserModel(**data)

    user.password = password_to_hash

    session.add(user)
    session.commit()

    return jsonify(user)

def verify_login():

    required_keys = ["email", "password"]

    data = request.get_json()

    if verify_missing_key(data, required_keys):
        raise MissingKeyError(data, required_keys)

    if verify_required_key(data, required_keys):
        raise RequiredKeyError(data, required_keys)

    user = UserModel.query.filter_by(email=data['email']).first()

    if not user:
        return {"message": "User not found"}, HTTPStatus.NOT_FOUND
    
    if user.verify_password(data['password']):
        access_token = create_access_token(identity=user)
        return {"message": access_token}
    else:
        return {"message": "Unauthorized"}, HTTPStatus.UNAUTHORIZED
