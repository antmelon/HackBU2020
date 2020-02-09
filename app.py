#Client ID 0oa24xlahiufsSAsx4x6
#Client Secret NQu4W7_u6RHTFhRR6ggKkgTxMpZn07j2yCdsNWbo
#Login token 00idk2KSs3hVXhksW2OBwKsaOVzJH6qVUF5OVPp8SL

from flask import Flask, render_template, g, redirect, url_for, flash
from .forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'e14a09eacbba9066f9dcae93dcabccda'

@app.route("/home")
def index():
    return render_template("index.html")


@app.route("/textbooks")
def getTextbooks():
    return render_template("textbooks.html")

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title = 'Register', form = form)

@app.route('/', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/home')
    return render_template('login.html', title='Sign In', form=form)
