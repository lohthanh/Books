from flask_app import app
from flask import render_template, redirect, request
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
    return render_template('one_book.html', one_book=one_book)