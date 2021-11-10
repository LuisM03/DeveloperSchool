from flask import render_template
from app import app, db
from app.schemas.models import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
