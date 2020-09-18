from flask import render_template, request
from app import app
from app.models.player import *
from app.models.game import *

@app.route('/')
def index():
    return render_template('index.html', title='game_name')