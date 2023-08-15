from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.author_model import Author
from flask_app.models.favorite_model import Favorite
from flask_app.models.book_model import Book

# View all authors
@app.route('/')
def authors():
    all_authors = Author.get_all_authors()
    return render_template('authors.html', all_authors=all_authors)

# Action route to create new author
@app.route('/authors/create_author', methods=['POST'])
def create_author():
    data = {
        **request.form
    }
    Author.create(data)
    return redirect('/')

# Route to view one author
@app.route('/authors/view/<int:id>')
def one_author(id):
    data = {
        'id' : id
    }
    one_author = Author.get_one_author(data)
    all_books = Book.get_all_books()
    authors_favorites = Favorite.get_all_favorites({'author_id': id})
    favorite_book_ids = [favorite['book_id'] for favorite in authors_favorites]
    return render_template('one_author.html', one_author=one_author, all_books=all_books, authors_favorites=authors_favorites,favorite_book_ids=favorite_book_ids)

# Action to add to favorites table
@app.route('/favorites', methods=['POST'])
def add_into_favorites():
    author_id = request.form.get('author_id')
    book_id = request.form['book_id']
    data = {
        'author_id': author_id,
        'book_id' : book_id
    }
    Favorite.create(data)
    return redirect(f'/authors/view/{author_id}')
