from flask import Blueprint, render_template, abort

platform = Blueprint('Platform', __name__, template_folder='templates')
