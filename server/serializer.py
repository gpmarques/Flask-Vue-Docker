from flask_marshmallow import Marshmallow
from models import Book

ma = Marshmallow()


class BookSchema(ma.ModelSchema):
    class Meta:
        model = Book
