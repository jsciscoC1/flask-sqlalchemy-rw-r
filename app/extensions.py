import logging

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from werkzeug.middleware.proxy_fix import ProxyFix

logger = logging.getLogger(__name__)

app = Flask(__name__, instance_relative_config=True)
app.wsgi_app = ProxyFix(app.wsgi_app)

db = SQLAlchemy(session_options={"autocommit": False, "autoflush": False})
migrate = Migrate(app, db)


# logger.info("Initting...")
# print("Inittiing...")
# init(app, db)


@app.route("/")
def hello():
    return "Hello, world!"
