from flask import Flask

def init_app(app: Flask):
    from .teste_view import bp as bp_teste

    app.register_blueprint(bp_teste)
