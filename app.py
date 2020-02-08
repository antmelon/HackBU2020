from flask import Flask
app = Flask(__name__)

@app.route("/textbooks")
def getTextbooks():
    return "Future home of textbooks"



def __init__():
    pass
