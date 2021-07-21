from app.models import AddressModel
from flask import current_app, request, jsonify


def update_address(user_id: int):

    required_keys = ["city", "state"]

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


def create(user_id):
    session =  current_app.db.session

    data = request.get_json()

    address = AddressModel(**data)

    address.user_id = user_id

    session.add(address)
    session.commit()

    return jsonify(address)



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

    return ""
