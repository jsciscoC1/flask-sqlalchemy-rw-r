import logging
import os

from app import service

logger = logging.getLogger(__name__)


def create_app():
    from .extensions import app

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("MASTER_DB")
    app.config["REPLICA"] = os.getenv("READ_REPLICAS")
    app.config["SQLALCHEMY_BINDS"] = {
        "master": os.getenv("MASTER_DB"),
        "replica": os.getenv("READ_REPLICAS"),
    }
    # app.config["SQLALCHEMY_POOL_SIZE"] = 10
    # app.config["SQLALCHEMY_POOL_RECYCLE"] = 1800
    # app.config["SQLALCHEMY_MAX_OVERFLOW"] = 20
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    from app.extensions import db

    # Required to generate migrations
    from .models.models import Book, Author

    db.init_app(app)

    from .api import api_blueprint as bp

    app.register_blueprint(bp)

    return app
