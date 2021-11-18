from flask import Blueprint, render_template, abort
from app.schemas.form import formRegister

formRegisterandLogin = Blueprint('formRegisterandLogin', __name__, template_folder='templates')

@formRegisterandLogin.route('/register')
def register():
    formReg = formRegister()
    return render_template('register.html', formReg = formReg)