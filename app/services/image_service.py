from re import T
from flask import current_app, jsonify, request
from http import HTTPStatus
import itertools

from app.models import ImageModel, ImageStyleModel, StyleModel, UserModel, AddressModel
from app.exc.missing_key import MissingKeyError
from app.exc.required_key import RequiredKeyError
from app.models import ImageModel, ImageStyleModel, StyleModel
from app.exc import MissingKeyError, RequiredKeyError

from app.services.helper_service import verify_required_key, verify_missing_key
from ipdb import set_trace

def create(user_id):

    session = current_app.db.session 

    data = request.get_json()

    image = ImageModel(**data)

    image.user_id = user_id

    session.add(image)
    session.commit()

    return jsonify(
        {
            "Image": image
        }
    ), HTTPStatus.CREATED


def delete(user_id: int):

    session = current_app.db.session

    found_img: ImageModel = ImageModel.query.filter_by(user_id=user_id).first()

    if not found_img:
        return {"status": "Image NOT FOUND"}, HTTPStatus.NOT_FOUND

    session.delete(found_img)
    session.commit()

    return {}


def update(img_id: int):

    required_keys = ["img_url", "description"]

    session = current_app.db.session

    data = request.get_json()

    if verify_required_key(data, required_keys):
        raise RequiredKeyError(data, required_keys)

    if verify_missing_key(data, required_keys):
        raise MissingKeyError(data, required_keys)

    found_img: ImageModel = ImageModel.query.get(img_id)

    if not found_img:
        return {"status": "Image NOT FOUND"}, HTTPStatus.NOT_FOUND

    for key, value in data.items():
        setattr(found_img, key, value)

    session.add(found_img)
    session.commit()

    return {
        "img_url": found_img.img_url,
        "description": found_img.description
    }


def get_images(user_id):

    images = ImageModel.query.filter_by(user_id=user_id).all()

    images = [
                {
                    "img_url": image.img_url,
                    "description": image.description,
                    "user_id": image.user_id,
                    "id": image.id,
                    "comments": f"/user/artist/{image.user_id}/image/{image.id}/comment",
                    "styles": image.this_styles,
                    "artist_profile": f"/user/artist/{image.user_id}"
                }
                
                for image in images
            ]

    return jsonify(images)
    

def get_image_by_id(image_id):

    image = ImageModel.query.get(image_id)
    
    if not image:
        return False

                
    image =     {
                    "img_url": image.img_url,
                    "description": image.description,
                    "user_id": image.user_id,
                    "id": image.id,
                    "comments": f"/user/artist/{image.user_id}/image/{image.id}/comment",
                    "styles": image.this_styles,
                    "artist_profile": f"/user/artist/{image.user_id}"
                }


    return jsonify(image)


def get_all_images():

    if request.args.get("style", type=str):
        style_name = request.args.get("style", type=str)

        style = StyleModel.query.filter(StyleModel.style_name.ilike(f"%{style_name}%")).first()
        image_styles = ImageStyleModel.query.filter_by(style_id=style.id).all()

        images = [
                    ImageModel.query.get(image.image_id) 
                    for image in image_styles
                ]
        

    elif request.args.get("city", type=str):
        city = request.args.get("city", type=str)

        addresses = AddressModel.query.filter(AddressModel.city.ilike(f"%{city}%")).all()

        users = [UserModel.query.get(address.user_id)
                    for address in addresses
                ]
        
        artists = [user for user in users if user.is_artist==True]

        images = [
                    ImageModel.query.filter_by(user_id=artist.id).all()
                    for artist in artists
                ]

        images = list(itertools.chain(*images))

    
    elif request.args.get("artist_name", type=str):
        try:
            artist_name = request.args.get("artist_name", type=str)
        
            user = UserModel.query.filter(UserModel.name.ilike(f"%{artist_name}%")).first()
            images = ImageModel.query.filter_by(user_id=user.id).all()

        except:
            return []

    else:
        images = ImageModel.query.all()


    images = [
                {
                    "img_url": image.img_url,
                    "description": image.description,
                    "user_id": image.user_id,
                    "id": image.id,
                    "comments": f"/user/artist/{image.user_id}/image/{image.id}/comment",
                    "styles": image.this_styles,
                    "artist_profile": f"/user/artist/{image.user_id}"

                }
                
                for image in images
            ]

    return images


def create_image_style(image_id, style_id):

    session = current_app.db.session

    image_style = ImageStyleModel(image_id=image_id, style_id=style_id)
    
    session.add(image_style)
    session.commit()
    
    return jsonify(image_style)


def get_styles():

    styles = StyleModel.query.all()

    return jsonify(styles)