from run import create_app
app = create_app('config')

from models import db
from models import Book
from serializer import BookSchema

with app.app_context():
    try:
        db.drop_all()

        db.create_all()

        BOOKS = [
            {
                'title': 'On the Road',
                'author': 'Jack Kerouac',
                'read': True
            },
            {
                'title': 'Harry Potter and the Philosopher\'s Stone',
                'author': 'J. K. Rowling',
                'read': False
            },
            {
                'title': 'Green Eggs and Ham',
                'author': 'Dr. Seuss',
                'read': True
            }
        ]
        book_serializer = BookSchema(many=True)
        books_data = book_serializer.load(BOOKS).data
        for book_data in books_data:
            db.session.add(book_data)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(str(e))