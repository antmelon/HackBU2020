#Client ID 0oa24xlahiufsSAsx4x6
#Client Secret NQu4W7_u6RHTFhRR6ggKkgTxMpZn07j2yCdsNWbo
#Login token 00idk2KSs3hVXhksW2OBwKsaOVzJH6qVUF5OVPp8SL

from flask import Flask, render_template, g, redirect, url_for, flash, session
from .forms import RegistrationForm, LoginForm, HasBookForm
import os, json
from .user import User, Textbook
from .main import createUser, addToBook, write_book, load_book, Book
import sys

has_loaded = False

file_path = os.path.abspath(os.getcwd())
app = Flask(__name__)


app.config['SECRET_KEY'] = 'e14a09eacbba9066f9dcae93dcabccda'

@app.route("/")
def index():
    user = session.get('user', None)
    print(user)
    return render_template("index.html")


@app.route("/textbooks")
def getTextbooks():
    return render_template("textbooks.html")

@app.route("/addbook", methods=['GET', 'POST'])
def addBook():
    book = load_book()
    form = HasBookForm()
    if form.validate_on_submit():
        print(book.textbooks)
        json_has_book = False
        for k,v in book.textbooks:
            if form.book_title.data in book.textbooks:
                print("changing")
                book.textbooks[form.book_title.data]['userArr'][-1]=((session.get('user', None)))
                json_has_book = True
        if not json_has_book:
            addToBook(book, Textbook(form.book_title.data, form.author.data, session.get('user', None)))
            print("registered book")
    write_book(book)
    return render_template('registerBook.html', title = 'Register Book', form= form)



@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Register requested for user {}'.format(
            form.username.data))
        new_user = User(form.username.data, form.password.data, form.full_name.data, form.email.data)
        createUser(new_user)
        session['user'] = form.username.data
        return redirect('/')
    return render_template('register.html', title = 'Register', form = form)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        #Loop through values in json file
        f = open("{file_path}/users.json".format(file_path=file_path))
        data = json.load(f)
        f.close()
        for (k, v) in data.items():
            if form.username.data == k:
                if form.password.data == v["password"]:
                    session['user'] = form.username.data

                    return redirect('/')
    return render_template('login.html', title='Sign In', form=form)
