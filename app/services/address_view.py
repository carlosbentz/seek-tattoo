from app.models import AddressModel

from http import HTTPStatus
from flask import current_app, request, jsonify


def update_address(address_id: int):

    session = current_app.db.session

    data = request.get_json()

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