from flask import Blueprint

from app.exc import RequiredKeyError, MissingKeyError

from app.services.user_delete_service import delete

from http import HTTPStatus

bp_user = Blueprint('user', __name__)

@bp_user.route('/user/<int:user_id>', methods=['DELETE'])
def update_user(user_id: int):

    try:
        return delete(user_id), HTTPStatus.OK
    
    except RequiredKeyError as e:
        return e.message

    except MissingKeyError as e:
        return e.message