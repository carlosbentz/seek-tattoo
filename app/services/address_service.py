from app.models import AddressModel

from http import HTTPStatus
from flask import current_app, request, jsonify

from app.services.helper_service import verify_required_key, verify_missing_key, verify_value_option

from app.exc.missing_key import MissingKeyError
from app.exc.required_key import RequiredKeyError


def update_address(address_id: int):

    required_keys = ["city", "style"]

    session = current_app.db.session

    data = request.get_json()

    if verify_missing_key(data, required_keys):
        raise MissingKeyError(data, required_keys)

    if verify_required_key(data, required_keys):
        raise RequiredKeyError(data, required_keys)

    found_address: AddressModel = AddressModel.query.get(address_id)

    if not found_address:
        return {"status": "Address NOT FOUND"}, HTTPStatus.NOT_FOUND

    for key, value in data.items():
        setattr(found_address, key, value)

    session.add(found_address)
    session.commit()

    output =  {
        "id": found_address.id,
        "city": found_address.city,
        "state": found_address.state
    }

    return jsonify(output)