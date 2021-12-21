from flask import Blueprint
from flask_restx import Api, Resource

from app import service

api_blueprint = Blueprint("api", __name__, url_prefix="/")
api = Api(
    api_blueprint,
    title="SQL Load Balancing Experiments",
    description="SQL Load Balancing Experiments",
)


class AuthorList(Resource):
    def get(self):
        return service.get_authors()


class AuthorDetail(Resource):
    pass


class BookList(Resource):
    pass


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
