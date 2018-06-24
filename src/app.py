from flask import Flask, render_template, request, session, redirect, url_for
from src.common.database import Database
import os
from src.models.users.views import user_bp

app = Flask(__name__)
app.config.from_object('src.config')

app.secret_key = str(os.environ.get('SECRET_KEY'))


@app.before_first_request
def initialize_database():
    Database.initialize()


@app.route('/')
def index():
    return render_template('index.html')


app.register_blueprint(user_bp, url_prefix='/users')
