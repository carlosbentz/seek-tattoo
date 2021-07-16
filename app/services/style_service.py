from flask import request, current_app

from app.services.helper_service import verify_required_key, verify_missing_key, verify_value_option

from app.models import StyleModel
from app.exc.missing_key import MissingKeyError
from app.exc.required_key import RequiredKeyError
from app.exc.different_value import InvalidOptionError

def verify_values():
    
    required_keys = ["style_name"]

    value_options = ["floral", "traço fino", "anime", "aquarela", "preto e branco", "realista", "abstrato", "colorido"]

    session = current_app.db.session

    data = request.get_json()

    style = data["style_name"]


    if verify_missing_key(data, required_keys):
        raise MissingKeyError(data, required_keys)

    if verify_required_key(data, required_keys):
        raise RequiredKeyError(data, required_keys)

    if not verify_value_option(data, value_options):
        raise InvalidOptionError(style, value_options)

    styles = StyleModel(**data)

    session.add(styles)
    session.commit()

    return {
        "style_name": styles.style_name
    }