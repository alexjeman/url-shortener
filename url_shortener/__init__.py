from flask import Flask
from . extensions import db
from . routes import short
from . auth import bp


def create_app(config_file='settings.py'):
    app = Flask(__name__)

    app.secret_key = 'secret'
    app.config.from_pyfile(config_file)

    db.init_app(app)

    app.register_blueprint(short)
    app.register_blueprint(bp)

    return app
