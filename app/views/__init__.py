from flask import Flask

def init_app(app: Flask):

    from .signup_view import bp as bp_signup

    app.register_blueprint(bp_signup)

    from .login_view import bp as bp_login

    app.register_blueprint(bp_login)

    from .user_view import bp as bp_user

    app.register_blueprint(bp_user)

    from .artist_view import bp as bp_artist

    app.register_blueprint(bp_artist)

    from .client_view import bp as bp_client

    app.register_blueprint(bp_client)

