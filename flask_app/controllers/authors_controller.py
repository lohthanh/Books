from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.author_model import Author

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
    return render_template('one_author.html', one_author=one_author)