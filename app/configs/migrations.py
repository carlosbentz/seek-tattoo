from flask_migrate import Migrate
from flask import Flask


mg = Migrate(compare_type="True")


def init_app(app: Flask):
    mg.init_app(app, app.db)
