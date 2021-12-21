from app.extensions import db


class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    author_id = db.Column(
        db.BigInteger, db.ForeignKey("authors.id"), nullable=False
    )


class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"{self.id}: {self.name}"
