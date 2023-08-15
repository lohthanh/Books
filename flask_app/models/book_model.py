from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB

class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def create(cls, data):
        query = """INSERT INTO books (title, num_of_pages) VALUES ( %(title)s, %(num_of_pages)s );"""
        return connectToMySQL(DB).query_db(query, data)
    
    @classmethod
    def get_all_books(cls):
        query = """SELECT * FROM books;"""
        return connectToMySQL(DB).query_db(query)
    
    @classmethod
    def get_one_book(cls, data):
        query = """SELECT * FROM books WHERE id = %(id)s;"""
        results = connectToMySQL(DB).query_db(query, data)
        if results:
            return cls(results[0])
        return False