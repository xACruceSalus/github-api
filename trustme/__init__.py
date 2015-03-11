from flask import Flask, render_template

from .extensions import config, oauth, assets
from .views.repos import repos
from .views.users import users


DEBUG = True
SECRET_KEY = 'super secret key'



def create_app():
    app = Flask(__name__)
    app.config.from_object(__name__)

    app.register_blueprint(repos)
    app.register_blueprint(users)

    config.init_app(app)
    oauth.init_app(app)
    assets.init_app(app)

    return app
