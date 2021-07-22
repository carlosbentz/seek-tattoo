from app.models import AddressModel
from flask import current_app, request, jsonify

from app.exc.missing_key import MissingKeyError
from app.exc.required_key import RequiredKeyError

from app.services.helper_service import verify_required_key, verify_missing_key

from http import HTTPStatus


def update_address(user_id: int):

    required_keys = ["city", "state"]

    session = current_app.db.session

    data = request.get_json()

    city = data.get("city")
    state = data.get("state")

    if verify_required_key(data, required_keys):
        raise RequiredKeyError(data, required_keys)

    if verify_missing_key(data, required_keys):
        raise MissingKeyError(data, required_keys)

    found_address: AddressModel = AddressModel.query.filter_by(user_id=user_id).first()

    if not found_address:
        return {"status": "Address NOT FOUND"}

    for key, value in data.items():
        setattr(found_address, key, value)

    session.add(found_address)
    session.commit()

    output =  {
        "city": found_address.city,
        "state": found_address.state
    }

    return jsonify(output)


def create(user_id):

    session =  current_app.db.session

    data = request.get_json()

    address = AddressModel(**data)

    address.user_id = user_id

    session.add(address)
    session.commit()

    return jsonify(address)

<<<<<<< HEAD

=======
>>>>>>> 1b7397246e9205c7aa478f11c32df32271a0bf03

def get_all():
    
    address = AddressModel.query.all()
    
    return jsonify(address)


def get_by_id(user_id: int):

    address = AddressModel.query.filter_by(user_id=user_id).first()

    return jsonify(address)


def delete(user_id):
    session = current_app.db.session

    address = AddressModel.query.filter_by(user_id=user_id).first()

    session.delete(address)
    session.commit()

    return "", HTTPStatus.NO_CONTENT
