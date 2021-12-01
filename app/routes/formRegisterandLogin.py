from flask import Blueprint, render_template, request
from app.schemas.form import formRegister


formRegisterandLogin = Blueprint('formRegisterandLogin', __name__, template_folder='templates')


@formRegisterandLogin.route('/register', methods=['GET', 'POST'])
def register():
    formReg = formRegister()

    if request.method == 'POST':
        name = request.form.get('name')
        lastname = request.form.get('lastname')
        documentsType = request.form.get('documentsType')
        documentsNumber = request.form.get('documentsNumber')
        email = request.form.get('email')
        age = request.form.get('age')
        gender = request.form.get('gender')
        password = request.form.get('password')
        rePassword = request.form.get('rePassword')

        if formReg.validate_on_submit():
            return continue_register()
        else:
            return 'Los parametros son incorrectos' ###Al igual que este mensaje.
        
    return render_template('register.html', formReg = formReg)



@formRegisterandLogin.route('/login')
def login():
    formReg = formRegister()
    return render_template('login.html', formReg = formReg)

@formRegisterandLogin.route('/continue_register')
def continue_register():
    formReg = formRegister()
    return render_template('continueRegister.html', formReg = formReg)