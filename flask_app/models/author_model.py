from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB

class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data):
        query = """INSERT INTO authors (name) VALUES ( %(name)s );"""
        return connectToMySQL(DB).query_db(query, data)

    @classmethod
    def get_all_authors(cls):
        query = """SELECT * FROM authors;"""
        return connectToMySQL(DB).query_db(query)