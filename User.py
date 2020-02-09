from .textbook import Textbook
class User:

    def __init__(self, name, password, fullname, email, textbooksWanted=[],textbooksHave = []):
        self.name = name;
        self.password = password
        self.fullname = fullname
        self.email = email
        self.textbooksWanted = textbooksWanted
        self.textbooksHave = textbooksHave
        #self.location = location

    def addTextbooksWanted(book):
        if len(self.textbooksWanted) == 0:
            self.textbooksWanted[0] = book
        else:
            self.textbooksWanted[-1] = book
    def addTextbooksHave(book):
        if len(self.textbooksHave) == 0:
            self.textbooksWHave[0] = book
        else:
            self.textbooksHave[-1] = book

    def getName(self):
        return self.name

    def getFullName(self):
        return self.fullname

    def getPassword(self):
        return self.password

    def getEmail(self):
        return self.email

    '''def getLocation(self):
        return self.location'''

    def getTextBooksWanted(self):
        return self.textbooksWanted

    def getTextBooksHave(self):
        return self.textbooksHave
