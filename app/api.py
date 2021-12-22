from flask import Blueprint, request
from flask_restx import Api, Resource

from app import service
from app.schemas import AuthorSchema, BookSchema

api_blueprint = Blueprint("api", __name__, url_prefix="/")
api = Api(
    api_blueprint,
    title="SQL Load Balancing Experiments",
    description="SQL Load Balancing Experiments",
)

author_schema = AuthorSchema()
book_schema = BookSchema()


class AuthorList(Resource):
    def get(self):
        return author_schema.dump(service.get_authors(), many=True)

    def post(self):
        return author_schema.dump(service.create_author(request.json))


class AuthorDetail(Resource):
    pass


class BookList(Resource):
    def get(self):
        return book_schema.dump(service.get_books(), many=True)

    def post(self):
        book = service.create_book(request.json)
        return book_schema.dump(book), 201


class BookDetail(Resource):
    pass


author_ns = api.namespace("author", description="author endpoints")
book_ns = api.namespace("book", description="book endpoints")
author_ns.add_resource(AuthorList, "/")
author_ns.add_resource(AuthorDetail, "/<int:author_id>")
book_ns.add_resource(BookList, "/")
book_ns.add_resource(BookDetail, "/<int:book_id>")

api.add_namespace(author_ns)
api.add_namespace(book_ns)
