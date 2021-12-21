import logging
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from app import service


logger = logging.getLogger(__name__)


def create_app():
    from .extensions import app

    app.config["MASTER_DB"] = os.getenv("MASTER_DB")
    app.config["REPLICA"] = os.getenv("READ_REPLICAS")
    app.config["SQLALCHEMY_POOL_SIZE"] = 10
    app.config["SQLALCHEMY_POOL_RECYCLE"] = 1800
    app.config["SQLALCHEMY_MAX_OVERFLOW"] = 20
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    from app.extensions import db

    # Required to generate migrations
    from .models.models import Book, Author

    db.init_app(app)

    master = create_engine(app.config["MASTER_DB"])
    replica = create_engine(app.config["REPLICA"])
    master_session = scoped_session(sessionmaker(bind=master))()
    replica_session = scoped_session(sessionmaker(bind=replica))()

    service.create_author("test", master_session)
    print(
        service.get_author("test", replica_session)
    )

    return app
