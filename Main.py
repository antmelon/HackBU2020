import json
from .user import User
from .textbook import Textbook
import os
data = {}
book = {}
file_path = os.path.abspath(os.getcwd())
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

def createTextbook(Textbook):
    book[Textbook.getTitle()] = {
        'title': Textbook.getTitle(),
        'author': Textbook.getAuthor(),
        'userArr': Textbook.getUserArr()
    }
    #cant add same textbook twice
    with open("{file_path}/books.json".format(file_path=file_path)) as f:
        write_data = json.load(f)

    write_data.update(data)

    with open("{file_path}/books.json".format(file_path=file_path), 'w') as f:
        json.dump(write_data, f)
