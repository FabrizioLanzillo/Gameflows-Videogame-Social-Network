import json
from json import JSONEncoder

#OBJECT CLASS FOR JSON
class Comments:
    def __init__(self, id=None, text=None, likes=None, date=None, author=None):
        self.id = id
        self.text = text
        self.likes = likes
        self.date = date
        self.author = author


# subclass JSONEncoder
class CommentsEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__