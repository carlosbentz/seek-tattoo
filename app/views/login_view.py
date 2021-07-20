from flask import Blueprint, request
from app.models.user_model import UserModel
from http import HTTPStatus
from flask_jwt_extended import create_access_token


bp = Blueprint('bp_login', __name__, url_prefix='/user')


@bp.post('/login')
def login():

    data = request.get_json()

    user = UserModel.query.filter_by(email=data['email']).first()

    if not user:
        return {"message": "User not found"}, HTTPStatus.NOT_FOUND
    
    if user.verify_password(data['password']):
        access_token = create_access_token(identity=user)
        return {"message": access_token}, HTTPStatus.OK
    else:
        return {"message": "Unauthorized"}, HTTPStatus.UNAUTHORIZED
