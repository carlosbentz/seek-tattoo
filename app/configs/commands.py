from flask import Flask
from flask.cli import AppGroup
from click import echo, argument
from datetime import datetime

from app.models import (
                            UserModel, 
                            AddressModel, 
                            DescriptionModel, 
                            CommentModel, 
                            StyleModel, 
                            ImageModel, 
                            ImageStyleModel
                        )


def cli_image_url(app: Flask):
    cli_image_url_group = AppGroup("image_url")
    session = app.db.session


    @cli_image_url_group.command("create")
    @argument("img_url")
    @argument("description")
    @argument("user_id")
    def create(img_url, description, user_id):
        image_url = ImageModel(img_url=img_url, description=description, user_id=user_id)

        session.add(image_url)
        session.commit()

        echo(f"Image created, link: {img_url}")


    @cli_image_url_group.command("print")
    def to_print():
        image_urls = ImageModel.query.all()
        
        # [echo(f"Link: {img_url.img_url}, Description: {img_url.description}") for img_url in image_urls]
        echo(image_urls[0].this_style)

    app.cli.add_command(cli_image_url_group)


def cli_description(app: Flask):
    cli_description_group = AppGroup("description")
    session = app.db.session


    @cli_description_group.command("create")
    @argument("experience")
    @argument("trait")
    @argument("paint")
    def create(experience, trait, paint):
        description = DescriptionModel(experience=experience, trait=trait, paint=paint)

        session.add(description)
        session.commit()
        echo(
            f"Description created, Experience: {description.experience}, Trait: {description.trait}, Paint: {description.paint}"
            )

    
    @cli_description_group.command("print")
    def to_print():
        descriptions = DescriptionModel.query.all()
        [
            echo(
                f"Experience: {description.experience}, Trait: {description.trait}, Paint: {description.paint}"
                ) for description in descriptions
        ]



    app.cli.add_command(cli_description_group) 


def cli_comment(app: Flask):
    cli_comment_group = AppGroup("comment")
    session = app.db.session


    @cli_comment_group.command("create")
    @argument("comment")
    @argument("user_id")
    def create(comment, user_id):
        date = datetime.now()

        comment = CommentModel(comment=comment, datetime=date, user_id=user_id)

        session.add(comment)
        session.commit()
        echo(
            f"Comment created, Comment: {comment.comment}, Date: {comment.datetime}, User id: {comment.user_id}"
            )

    
    @cli_comment_group.command("print")
    def to_print():
        comments = CommentModel.query.all()
        [
            echo(
                f"Comment: {comment.comment}, Date: {comment.datetime}, User id: {comment.user_id}"
                ) for comment in comments
        ]



    app.cli.add_command(cli_comment_group) 


def cli_comment(app: Flask):
    cli_comment_group = AppGroup("comment")
    session = app.db.session


    @cli_comment_group.command("create")
    @argument("comment")
    @argument("user_id")
    @argument("image_id")
    def create(comment, user_id, image_id):
        date = datetime.now()

        comment = CommentModel(comment=comment, datetime=date, user_id=user_id, image_id=image_id)

        session.add(comment)
        session.commit()
        echo(
            f"Comment created, Comment: {comment.comment}, Date: {comment.datetime}, User id: {comment.user_id}, Image Id: {comment.image_id}"
            )

    
    @cli_comment_group.command("print")
    def to_print():
        comments = CommentModel.query.all()
        [
            echo(
                f"Comment: {comment.comment}, Date: {comment.datetime}, User id: {comment.user_id}, Image Id: {comment.image_id}"
                ) for comment in comments
        ]


    app.cli.add_command(cli_comment_group) 


def cli_address(app: Flask):
    cli_address_group = AppGroup("address")
    session = app.db.session


    @cli_address_group.command("create")
    @argument("city")
    @argument("state")
    @argument("user_id")
    def create(city, state, user_id):
        address = AddressModel(city=city, state=state, user_id=user_id)

        session.add(address)
        session.commit()
        echo(
            f"Address created, City: {address.city}, State: {address.state}, User Id: {address.user_id}"
            )

    
    @cli_address_group.command("print")
    def to_print():
        addresses = AddressModel.query.all()
        [
            echo(
                f"City: {address.city}, State: {address.state}, User Id: {address.user_id}"
                ) for address in addresses
        ]


    app.cli.add_command(cli_address_group) 


def cli_style(app: Flask):
    cli_style_group = AppGroup("style")
    session = app.db.session


    @cli_style_group.command("create")
    @argument("style_name")
    def create(style_name):
        style = StyleModel(style_name=style_name)

        session.add(style)
        session.commit()
        echo(
            f"Style created, Name: {style.style_name}"
            )

    
    @cli_style_group.command("print")
    def to_print():
        styles = StyleModel.query.all()
        [
            echo(
                f"Style name: {style.style_name}"
                ) for style in styles
        ]


    app.cli.add_command(cli_style_group) 


def cli_image_style(app: Flask):
    cli_image_style_group = AppGroup("image_style")
    session = app.db.session


    @cli_image_style_group.command("create")
    @argument("image_id")
    @argument("style_id")
    def create(image_id, style_id):
        image_style = ImageStyleModel(image_id=image_id, style_id=style_id)

        session.add(image_style)
        session.commit()
        echo(
            f"Image-Style created, Image Id: {image_style.image_id}, Style Id: {image_style.style_id}"
            )

    
    @cli_image_style_group.command("print")
    def to_print():
        image_styles = ImageStyleModel.query.all()
        [
            echo(
                f"Image Id: {image_style.image_id}, Style Id: {image_style.style_id}"
                ) for image_style in image_styles
        ]


    app.cli.add_command(cli_image_style_group)


def cli_user(app: Flask):
    cli_user_group = AppGroup("user")
    session = app.db.session


    @cli_user_group.command("create")
    @argument("name")
    @argument("email")
    @argument("password")
    def create(name, email, password):
        password_to_hash = password

        user = UserModel(name=name, email=email)

        user.password = password_to_hash

        session.add(user)
        session.commit()
        echo(
            f"User created, Name: {user.name}, Email: {user.email}, Password Hash: {user.password_hash}, Is Artist: {user.is_artist}"
            )


    @cli_user_group.command("create_artist")
    @argument("name")
    @argument("email")
    @argument("password")
    def create(name, email, password):
        password_to_hash = password

        user = UserModel(name=name, email=email, is_artist=True)

        user.password = password_to_hash

        session.add(user)
        session.commit()
        echo(
            f"Artist created, Name: {user.name}, Email: {user.email}, Password Hash: {user.password_hash}, Is Artist: {user.is_artist}"
            )

    
    @cli_user_group.command("print")
    def to_print():
        users = UserModel.query.all()
        [
            echo(
                f"Name: {user.name}, Email: {user.email}, Password Hash: {user.password_hash}, Is Artist: {user.is_artist}"
                ) for user in users
        ]


    app.cli.add_command(cli_user_group) 

def init_app(app: Flask):
    cli_image_url(app)
    cli_description(app)
    cli_comment(app)
    cli_address(app)
    cli_style(app)
    cli_image_style(app)
    cli_user(app)
