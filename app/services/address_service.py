from app.models import AddressModel

from http import HTTPStatus
from flask import current_app, request, jsonify

from app.services.helper_service import verify_required_key, verify_missing_key, verify_value_option

from app.exc.missing_key import MissingKeyError
from app.exc.required_key import RequiredKeyError


def update_address(user_id: int):

    # required_keys = ["city", "state"]

    data = request.get_json()

    city = data.get("city")
    state = data.get("state")

    session = current_app.db.session

    found_address: AddressModel = AddressModel.query.filter_by(user_id=user_id).first()

    if not found_address:
        return {"status": "Address NOT FOUND"}

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