from marshmallow_sqlalchemy import ModelSchema

from app.models import models


class AuthorSchema(ModelSchema):
    class Meta:
        fields = ("id", "name")

        model = models.Author
