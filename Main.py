import json
import User
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
        'Location': User.getLocation(),
        'TextBooks Have': User.getTextBooksHave()
    }
    jsondata = json.dumps(data)
    with open("{file_path}/users.json".format(file_path=file_path), "w") as f:
        f.write(jsondata)
        f.close()
def createTextbook(User):
    book[Textbook.getName()] = {
        'title': Textbook.getTitle(),
        'author': Textbook.getAuthor(),
        'userArr': Textbook.getUserArr()
    }
    #cant add same textbook twice
    jsondata = json.dumps(book)
    with open("{file_path}/books.json".format(file_path=file_path), "w") as f:
        f.write(jsondata)
        f.close()
