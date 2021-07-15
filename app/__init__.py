from flask import Flask
from environs import Env

from app.configs import database, migrations, commands
from app import views

env = Env()
env.read_env()


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = env("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JSON_SORT_KEYS"] = False

    database.init_app(app)
    migrations.init_app(app)
    views.init_app(app)
    commands.init_app(app)

    return app
