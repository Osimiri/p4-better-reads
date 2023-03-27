#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from flask_restful import Api, Resource

# Local imports
from config import app, db, api
from models import Author, Genre, User, UserBook, Book

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)

# Views go here!

@app.route('/')
def index():
    return '<h1>Welcome to Better Reads</h1>'

@app.route('/authors', methods = ['GET'])
def author():
    authors = Author.query.all()
    authors_dict =  [author.to_dict() for author in authors]

    response = make_response(
        jsonify(authors_dict),
        200
    )

    return response 

@app.route('/genres', methods = ['GET'])
def genres():
    genres = Genre.query.all()
    genres_dict =  [genre.to_dict() for genre in genres]

    response = make_response(
        jsonify(genres_dict),
        200
    )

    return response 

@app.route('/users', methods = ['GET'])
def users():
    users = User.query.all()
    users_dict =  [user.to_dict() for user in users]

    response = make_response(
        jsonify(users_dict),
        200
    )

    return response 

@app.route('/books', methods = ['GET'])
def books():
    books = Book.query.all()
    books_dict =  [book.to_dict() for book in books]

    response = make_response(
        jsonify(books_dict),
        200
    )

    return response 

@app.route('/userbooks', methods = ['GET'])
def userbooks():
    user_books = UserBook.query.all()
    user_books_dict =  [user_book.to_dict() for user_book in user_books]

    response = make_response(
        jsonify(user_books_dict),
        200
    )

    return response 

if __name__ == '__main__':
    app.run(port=5555, debug=True)
