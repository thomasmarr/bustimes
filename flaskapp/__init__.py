from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mongoengine import MongoEngine
from config import config

db = SQLAlchemy()
mongodb = MongoEngine()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    mongodb.init_app(app)

    from .main import main_blueprint
    from .api import api_blueprint
    from .error import error_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(error_blueprint)
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
