import logging
import os

from app import service

logger = logging.getLogger(__name__)


def parse_replicas():
    replicas = os.getenv("READ_REPLICAS").split(',')
    print(replicas)
    return replicas


def create_app():
    from .extensions import app

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("MASTER_DB")
    app.config["REPLICA"] = os.getenv("READ_REPLICAS")
    # Need to parse READ_REPLICAS which will be a comma delimited list of replicas
    # and bind them appropriately
    replicas = parse_replicas()
    app.config["SQLALCHEMY_BINDS"] = {
        "master": os.getenv("MASTER_DB")
    }
    app.config["REPLICA_SET"] = []
    for idx, replica in enumerate(replicas):
        app.config['SQLALCHEMY_BINDS'][f'replica_{idx}'] = replica
        app.config["REPLICA_SET"].append(f'replica_{idx}')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    from app.extensions import db, replicated

    # Required to generate migrations
    from .models.models import Book, Author

    db.init_app(app)
    replicated.init_app(app)

    from .api import api_blueprint as bp

    app.register_blueprint(bp)

    return app
