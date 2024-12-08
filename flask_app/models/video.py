from ..config.mysqlconnection import connectToMySQL

class Video:
    def __init__(self,data):
        self.id = data['id']
        self.url = data['url']
        self.button = data['button']

    @classmethod
    def get(cls):
        query = "SELECT * FROM video where id = 1;"
        results = connectToMySQL('ra').query_db(query)
        if len(results) > 0:
            return results[0]
        else:
            return None

    @classmethod
    def update(cls, data):
        query = "UPDATE video SET url = %(url)s, button = %(button)s WHERE id = 1"
        return connectToMySQL('ra').query_db(query, data)
    