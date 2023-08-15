
from flask import Flask
app = Flask(__name__)
app.secret_key = "shhhhhh"
DB = 'books_and_authors_schema'