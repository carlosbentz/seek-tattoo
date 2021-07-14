from flask import Blueprint

from app.exc import RequiredKeyError, MissingKeyError

from app.services.user_patch_service import update

from http import HTTPStatus

bp_user = Blueprint('user', __name__)

@bp_user.route('/user/<int:user_id>', methods=['PATCH'])
def update_user(user_id):

    try:
        return update(user_id), HTTPStatus.OK
    
    except RequiredKeyError as e:
        return e.message

    except MissingKeyError as e:
        return e.message