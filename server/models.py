from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    read = db.Column(db.Boolean, nullable=False)

    def __init__(self, title, author, read):
        self.title = title
        self.author = author
        self.read = read
