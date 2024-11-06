from flask import flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

db: SQLAlchemy = SQLAlchemy()
migrate: Migrate = Migrate

def crear_app() -> flask:
    app = flask(__name__)
    app.config.from_object(config)

    db.init_app(app)

    # import ... from ...
    # app.register_blueprint() 
    return app