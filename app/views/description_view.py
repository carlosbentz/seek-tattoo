from flask import Blueprint, request, jsonify, current_app
from app import exc
from app.models import DescriptionModel
from app.exc import RequiredKeyError, MissingKeyError
from app.services.description_service import update_description_id_in_user, update_description
from flask_jwt_extended import jwt_required
import ipdb

from http import HTTPStatus


bp = Blueprint('bp_description', __name__, url_prefix="/user")


@bp.post("/artist/<user_id>/description")
def create_artist(user_id: int):

    session =  current_app.db.session
    data = request.get_json()

    description = DescriptionModel(**data)

    session.add(description)
    session.commit()

    update_description_id_in_user(user_id, description.id)
    
    return jsonify(description),  HTTPStatus.CREATED



@bp.patch("/artist/<user_id>/description")
@jwt_required()
def patch_description(user_id: int):

    try:
        return update_description(user_id), HTTPStatus.OK
    
    except RequiredKeyError as e:
        return e.message

    except MissingKeyError as e:
        return e.message

# DELETE deleta o cadastro de artista e muda na tabela user is_artist=FALSE