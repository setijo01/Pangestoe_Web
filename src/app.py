from flask import Flask, render_template, request, session, redirect, url_for
from src.common.database import Database
from src.models.entries.entry import Entry
import os

app = Flask(__name__)
app.config.from_object('src.config')

app.secret_key = str(os.environ.get('SECRET_KEY'))


@app.before_first_request
def initialize_database():
    Database.initialize()
    session['user_email'] = None


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/gallery')
def gallery():
    return render_template('gallery_view.html')