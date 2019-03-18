from flask import Flask


def create_app(config_file):

    app = Flask(__name__)
    app.config.from_object(config_file)

    from models import db
    db.init_app(app)
    print('init db')

    from serializer import ma
    ma.init_app(app)
    print('init serializer')

    from flask_cors import CORS
    CORS(app)
    print('CORS')

    from books import book_blueprint
    app.register_blueprint(book_blueprint)
    print('book_blueprint')

    return app


app = create_app('config')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000')
