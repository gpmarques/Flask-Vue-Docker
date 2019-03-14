from flask import Blueprint
from flask import jsonify
from flask import request
from models import db
from models import Book
from serializer import BookSchema
import uuid

book_blueprint = Blueprint('books', __name__)


@book_blueprint.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    print(request.method)
    if request.method == 'POST':
        try:
            post_data = request.get_json()
            schema = BookSchema()
            new_book = schema.load(post_data).data
            db.session.add(new_book)
            db.session.commit()
            response_object['message'] = 'Book added!'
        except Exception as e:
            db.session.rollback()
            print(str(e))
            response_object['status'] = 'false'

    if request.method == 'GET':
        schema = BookSchema(many=True)
        books = Book.query.order_by(Book.id).all()
        response_object['books'] = schema.dump(books)

    return jsonify(response_object)


@book_blueprint.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    response_object = {'status': 'success'}
    book = Book.query.get(book_id)

    if request.method == 'PUT':
        put_data = request.get_json()
        book.author = put_data['author']
        book.title = put_data['title']
        book.read = put_data['read']
        db.session.commit()
        response_object['message'] = 'Book updated!'

    if request.method == 'DELETE':
        db.session.delete(book)
        db.session.commit()
        response_object['message'] = 'Book removed!'
    return jsonify(response_object)


