#Client ID 0oa24xlahiufsSAsx4x6
#Client Secret NQu4W7_u6RHTFhRR6ggKkgTxMpZn07j2yCdsNWbo
#Login token 00idk2KSs3hVXhksW2OBwKsaOVzJH6qVUF5OVPp8SL

from flask import Flask, render_template, g, redirect, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET KEY'] = 'e14a09eacbba9066f9dcae93dcabccda'

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/textbooks")
def getTextbooks():
    return "Future home of textbooks"

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title = 'Register', form = form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Login', form = form)
