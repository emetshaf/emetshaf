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


@app_views.route('/books/<book_id>/authors', methods=['GET'])
def get_authors(book_id):
    """books route to handle http method for requested books by city
    """
    book_obj = storage.get('Book', book_id)
    if book_obj is None:
        abort(404)
    all_authors = storage.all('Author')
    book_authors = book_obj.authors
    book_authors = [obj.to_json() for obj in book_authors]
    return jsonify(book_authors)


@app_views.route('/books/<book_id>/reviews', methods=['GET'])
def get_reviews(book_id):
    """books route to handle http method for requested books by city
    """
    book = storage.get('Book', book_id)
    if book is None:
        abort(404)
    all_reviews = storage.all('Review')
    book_reviews = [obj.to_json() for obj in all_reviews.values()
                    if obj.book_id == book_id]
    return jsonify(book_reviews)
