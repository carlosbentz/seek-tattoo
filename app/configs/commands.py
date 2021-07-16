from flask import Flask
from flask.cli import AppGroup
from click import echo


def cli_teste(app: Flask):
    cli_teste_group = AppGroup("teste")

    
    @cli_teste_group.command("print")
    def printar():
        echo("Exemplo de texto.")


    app.cli.add_command(cli_teste_group)

def init_app(app: Flask):
    cli_teste(app)
