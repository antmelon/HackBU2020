class Textbook:
    def __init__(self, title, author, UserArr):
        self.title = title
        self.author = author
        self.UserArr = [UserArr]



    def getTitle(self):
        return self.title


    def getAuthor(self):
        return self.author


    def getUserArr(self):
        return self.UserArr
