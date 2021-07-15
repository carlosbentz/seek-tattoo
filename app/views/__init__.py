from flask import Flask

def init_app(app: Flask):
    from .teste_view import bp as bp_teste

    app.register_blueprint(bp_teste)

    from .signup_view import bp as bp_signup

    app.register_blueprint(bp_signup)

    from .login_view import bp as bp_login

    app.register_blueprint(bp_login)
