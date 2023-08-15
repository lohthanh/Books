from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.author_model import Author
from flask_app.models.favorite_model import Favorite
from flask_app.models.book_model import Book

# View all books
@app.route('/books')
def books():
    all_books = Book.get_all_books()
    return render_template('books.html', all_books=all_books)

# Action to add new books
@app.route('/books/create_book', methods=['POST'])
def create_book():
    data = {
        **request.form
    }
    Book.create(data)
    return redirect('/books')

# Route to view one book
@app.route('/books/view/<int:id>')
def one_book(id):
    data = {
        'id' : id
    }
    one_book = Book.get_one_book(data)
    all_authors = Author.get_all_authors()
    books_favorites = Favorite.get_all_favorites_by_books({'book_id': id})
    favorite_book_ids = [favorite['author_id'] for favorite in books_favorites]
    return render_template('one_book.html', favorite_book_ids=favorite_book_ids, one_book=one_book, all_authors=all_authors, books_favorites=books_favorites)

# Action to add to favorites
@app.route('/favorites/books', methods=['POST'])
def add_authors_into_books():
    author_id = request.form.get('author_id')
    book_id = request.form['book_id']
    data = {
        'author_id': author_id,
        'book_id' : book_id
    }
    Favorite.create(data)
    return redirect(f'/books/view/{book_id}')
