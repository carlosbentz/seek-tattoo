from flask import Blueprint

from app.exc import RequiredKeyError, MissingKeyError
from app.services.user_service import delete, update

from http import HTTPStatus

bp = Blueprint('bp_user', __name__)

@bp.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id: int):

    try:
        return delete(user_id), HTTPStatus.OK
    
    except RequiredKeyError as e:
        return e.message

    except MissingKeyError as e:
        return e.message

"""
sqlalchemy.exc.IntegrityError: (psycopg2.errors.NotNullViolation) null value in column "user_id" of relation "addresses" violates not-null constraint
DETAIL:  Failing row contains (1, Curitiba, PR, null).
Viola as regras
"""


@bp.route('/user/<int:user_id>', methods=['PATCH'])
def update_user(user_id):

    try:
        return update(user_id), HTTPStatus.OK
    
    except RequiredKeyError as e:
        return e.message

    except MissingKeyError as e:
        return e.message