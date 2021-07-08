from flask import Flask
from flask.cli import AppGroup
from click import echo, argument
from app.models import (
                            StyleModel, 
                            DescriptionModel, 
                            ImageModel, 
                            UserModel,
                            AddressModel, 
                            CommentModel, 
                            ImageStyleCommentsModel, 
                        )


def cli_teste(app: Flask):
    cli_teste_group = AppGroup("teste")

    
    @cli_teste_group.command("print")
    def printar():
        echo("Exemplo de texto.")


    app.cli.add_command(cli_teste_group)


def cli_image_url(app: Flask):
    cli_image_url_group = AppGroup("image_url")
    session = app.db.session


    @cli_image_url_group.command("create")
    @argument("img_url")
    @argument("description")
    def create(img_url, description):
        try:
            image_url = ImageModel(img_url=img_url, description=description)

            session.add(image_url)
            session.commit()
            echo(f"Image created, link: {img_url}")
        except:
            echo("Erro ao criar")

    @cli_image_url_group.command("print")
    def to_print():
        image_urls = ImageModel.query.all()
        [echo(f"Link: {img_url.link}, Description: {img_url.description}") for img_url in image_urls]

    app.cli.add_command(cli_image_url_group)


def init_app(app: Flask):
    cli_teste(app)
    cli_image_url(app)
