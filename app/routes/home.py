from flask import Blueprint, render_template, abort

page_home = Blueprint('Home', __name__, template_folder='templates')

@page_home.route('/')
@page_home.route('/home')
def home():
    return render_template('index.html')