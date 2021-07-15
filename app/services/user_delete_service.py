from app.models.user_model import UserModel

from http import HTTPStatus
from app import db

def delete(user_id: int):

    found_user = UserModel.query.get(user_id)

    if not found_user:
        return {"status": "User NOT FOUND"}, HTTPStatus.NOT_FOUND

    db.session.delete(found_user)
    db.session.commit()

    return {}, HTTPStatus.NO_CONTENT
