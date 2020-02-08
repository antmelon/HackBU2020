#Client ID 0oa24xlahiufsSAsx4x6
#Client Secret NQu4W7_u6RHTFhRR6ggKkgTxMpZn07j2yCdsNWbo
#Login token 00idk2KSs3hVXhksW2OBwKsaOVzJH6qVUF5OVPp8SL

from flask import Flask, render_template, g, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/textbooks")
def getTextbooks():
    return "Future home of textbooks"
