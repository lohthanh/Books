from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB

class Favorite:
    def __init__(self, data):
        self.author_id = data['author_id']
        self.user_id = data['user_id']

    