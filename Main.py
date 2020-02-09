import json
from .user import User
from .textbook import Textbook
import os, sys
data = {}
file_path = os.path.abspath(os.getcwd())

class BookSerializer(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Book):
            return o.textbooks
        if isinstance(o, Textbook):
            return {k: v for k, v in o.__dict__.items() if k in vars(o)}
        return super().default(o)

class Book(object):
    def __init__(self):
        self.textbooks = {}

def load_book():
    book = Book()
    try:
        f = open("{file_path}/books.json".format(file_path=file_path), 'r')
        temp = json.load(f)
        for (t, v) in temp:
            book.textbooks[t] = Textbook(t, v['author'], v['userArr'])
        f.close()
    except:
        pass
    return book

def write_book(book):
    with open("{file_path}/books.json".format(file_path=file_path), 'w') as f:
        json.dump(book, f, cls=BookSerializer, indent=4)


def createUser(User):
    data[User.getName()] = {
        'name': User.getName(),
        'password': User.getPassword(),
        'Full Name': User.getFullName(),
        'email': User.getEmail(),
        'TextBooks Wanted': User.getTextBooksWanted(),
        #'Location': User.getLocation(),
        'TextBooks Have': User.getTextBooksHave()
    }
    with open("{file_path}/users.json".format(file_path=file_path)) as f:
        write_data = json.load(f)

    write_data.update(data)

    with open("{file_path}/users.json".format(file_path=file_path), 'w') as f:
        json.dump(write_data, f)

def addToBook(book, t):
    book.textbooks[t.title] = t
    #write_to_json()
