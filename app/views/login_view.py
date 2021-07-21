from flask import Blueprint
from http import HTTPStatus

from app.exc import RequiredKeyError, MissingKeyError
from app.services.user_service import verify_login


bp = Blueprint('bp_login', __name__, url_prefix='/user')


@bp.post('/login')
def login():

    try:
        return verify_login(), HTTPStatus.OK
    
    except RequiredKeyError as e:
        return e.message

    except MissingKeyError as e:
        return e.message
