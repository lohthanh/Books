from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.author_model import Author

# View all authors
@app.route('/authors')
def authors():
    all_authors = Author.get_all_authors()
    return render_template('authors.html', all_authors=all_authors)