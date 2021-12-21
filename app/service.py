import json

from app.models.models import Author
from .extensions import db


def create_author(data):
    author = Author()
    author.name = data["name"]
    print(db.engine)
    db.session.add(author)
    db.session.commit()
    return author


def get_author(name: str, session):
    return session.query(Author).filter_by(name=name).all()


def get_authors():
    # # TODO: This is kind of wrong.
    # e = db.get_engine(app=current_app, bind="replica")
    # print(e)
    # Session = sessionmaker(e)
    # with Session() as session:
    #     return session.query(Author).all()
    print(db.engine)
    return db.session.query(Author).all()
