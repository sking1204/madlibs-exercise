from flask import Flask, request, render_template
from random import randint, choice, sample

from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY']="catsarecool1234"
debug = DebugToolbarExtension(app)