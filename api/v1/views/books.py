#!/usr/bin/python3
"""
Flask route that returns json status response
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from flasgger.utils import swag_from
from models import CNC, storage, User


@app_views.route('/books', methods=['GET'])
def all_books():
    """books route to handle http method for requested books by city
    """
    all_books = storage.all('Book')
    all_books = list(obj.to_json() for obj in all_books.values())
    return jsonify(all_books)


@app_views.route('/books/<book_id>', methods=['GET'])
def get_book(book_id):
    """books route to handle http method for requested books by city
    """
    book = storage.get('Book', book_id)
    if book is None:
        abort(404)
    return jsonify(book.to_json())
