from app.models.models import Author


def create_author(name: str, session):
    author = Author()
    author.name = name

    session.add(author)
    session.commit()


def get_author(name: str, session):
    return session.query(Author).filter_by(name=name).all()
