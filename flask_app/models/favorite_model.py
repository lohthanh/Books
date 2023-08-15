from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB

class Favorite:
    def __init__(self, data):
        self.author_id = data['author_id']
        self.book_id = data['book_id']

    @classmethod
    def create(cls, data):
        query = """INSERT INTO favorites (author_id, book_id) VALUES ( %(author_id)s, %(book_id)s );"""
        return connectToMySQL(DB).query_db(query, data)
    
    @classmethod
    def get_all_favorites(cls, data):
        query = """SELECT * FROM favorites JOIN books ON favorites.book_id = books.id WHERE favorites.author_id = %(author_id)s ORDER BY books.title;"""
        return connectToMySQL(DB).query_db(query, data)
    
    @classmethod
    def get_all_favorites_by_books(cls, data):
        query = """SELECT * FROM favorites JOIN authors ON favorites.author_id = authors.id WHERE favorites.book_id = %(book_id)s ORDER BY authors.name;"""
        return connectToMySQL(DB).query_db(query, data)