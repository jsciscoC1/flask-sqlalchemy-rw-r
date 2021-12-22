import json

from app.models.models import Author, Book
from .extensions import db


def create_author(data):
    author = Author()
    author.name = data["name"]
    print(db.engine)
    db.session.add(author)
    db.session.commit()
    return author


def get_authors():
    print(db.engine)
    return db.session.query(Author).all()


def get_books():
    print(db.engine)
    return db.session.query(Book).all()


def create_book(data):
    book = Book()
    book.author_id = data['author_id']
    book.name = data['name']
    print(db.engine)
    db.session.add(book)
    db.session.commit()
    return book
