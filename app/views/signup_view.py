from app.services.user_service import signup
from flask import Blueprint, request, current_app, jsonify

from http import HTTPStatus

from app.models.user_model import UserModel

from app.services.helper_service import verify_required_key, verify_missing_key

from app.exc.missing_key import MissingKeyError
from app.exc.required_key import RequiredKeyError

bp = Blueprint('bp_signup', __name__, url_prefix='/user')


@bp.post('/signup')
def create():

    try:
        return signup(), HTTPStatus.OK
    
    except RequiredKeyError as e:
        return e.message

    except MissingKeyError as e:
        return e.message

