from flask import Blueprint, request, current_app, jsonify
from app.models.user_model import UserModel
from http import HTTPStatus


bp = Blueprint('bp_signup', __name__, url_prefix='/user')


@bp.post('/signup')
def create():
    session =  current_app.db.session

    data = request.get_json()

    password_to_hash = data.pop('password')

    user = UserModel(**data)

    user.password = password_to_hash

    session.add(user)
    session.commit()

    return jsonify(user), HTTPStatus.CREATED
