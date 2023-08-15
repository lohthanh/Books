from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB

class Favorite:
    def __init__(self, data):
        self.author_id = data['author_id']
        self.user_id = data['user_id']

    @classmethod
    def create(cls, data):
        query = """INSERT INTO favorites (author_id, user_id) VALUES ( %(author_id)s, %(user_id)s );"""
        return connectToMySQL(DB).query_db(query, data)