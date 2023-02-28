"""
Flask route that returns json status response
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from flasgger.utils import swag_from
from models import CNC, storage, User


@app_views.route('/books', methods=['GET'], strict_slashes=False)
def all_books():
    """books route to handle http method for requested books by city
    """
    all_books = storage.all('Book')
    all_books = list(obj.to_json() for obj in all_books.values())
    return jsonify(all_books)


@app_views.route('/books', methods=['POST'], strict_slashes=False)
def create_book():
    """books route to handle http method for requested books by city
    """
    req_data = request.get_json()
    if req_data is None:
        abort(400, 'Not a JSON')
    if req_data.get('title') is None:
        abort(400, 'Missing title')
    if req_data.get('author_id') is None:
        abort(400, 'Missing author_id')
    if req_data.get('description') is None:
        abort(400, 'Missing description')
    if req_data.get('language') is None:
        abort(400, 'Missing language')
    Book = CNC.get('Book')
    new_book = Book(**req_data)
    new_book.save()
    return jsonify(new_book.to_json()), 201


@app_views.route('/books/<book_id>/authors/<author_id>', methods=['POST'], strict_slashes=False)
def add_author(book_id, author_id):
    """books route to handle http method for requested books by city
    """
    book = storage.get('Book', book_id)
    author = storage.get('Author', author_id)
    if book is None:
        abort(404)
    if author is None:
        abort(404)
    book.authors.append(author)
    book.save()
    return jsonify(book.to_json()), 201


@app_views.route('/books/<book_id>/authors/<author_id>', methods=['DELETE'], strict_slashes=False)
def delete_author_by_bood_id(book_id, author_id):
    """books route to handle http method for requested books by city
    """
    book = storage.get('Book', book_id)
    author = storage.get('Author', author_id)
    if book is None:
        abort(404)
    if author is None:
        abort(404)
    book.authors.remove(author)
    book.save()
    return jsonify(book.to_json()), 201


@app_views.route('/books/<book_id>', methods=['GET'], strict_slashes=False)
def get_book(book_id):
    """books route to handle http method for requested books by city
    """
    book = storage.get('Book', book_id)
    if book is None:
        abort(404)
    return jsonify(book.to_json())


@app_views.route('/books/<book_id>/authors', methods=['GET'], strict_slashes=False)
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


@app_views.route('/books/<book_id>/reviews', methods=['GET'], strict_slashes=False)
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


@app_views.route('/books_search', methods=['POST'], strict_slashes=False)
def search_books():
    """books route to handle http method for requested books by city
    """
    req_data = request.get_json()
    if req_data is None:
        abort(400, 'Not a JSON')
    if req_data.get('search') is None:
        abort(400, 'Missing search')
    search = req_data.get('search')
    all_books = storage.all('Book')
    all_books = [obj.to_json() for obj in all_books.values()]
    if search == '':
        return jsonify(all_books)
    search_books = [book for book in all_books if search in book['title']]
    return jsonify(search_books)
