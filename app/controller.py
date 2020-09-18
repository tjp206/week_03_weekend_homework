from flask import render_template, request
from app import app
from app.models.player import import *
from app.models.game import *

@app.route('/')
def index():
    return render_template('index.html', title='Home', ) #rock_paper_scissors = rock_paper_scissors?