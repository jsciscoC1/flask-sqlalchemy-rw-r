from flask import current_app
from sqlalchemy.orm import sessionmaker

from app.models.models import Author
from .extensions import db


def create_author(name: str, session):
    author = Author()
    author.name = name

    session.add(author)
    session.commit()


def get_author(name: str, session):
    return session.query(Author).filter_by(name=name).all()


def get_authors():
    e = db.get_engine(app=current_app, bind="replica")
    print(e)
    Session = sessionmaker(e)
    with Session() as session:
        return session.query(Author).all()
