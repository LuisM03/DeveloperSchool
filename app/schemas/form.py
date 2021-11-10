from flask_wtf import FlaskForm
from wtforms import Form, IntegerField,SelectField,SubmitField,StringField
from wtforms import validators
from wtforms.fields.html5 import EmailField
from wtforms.fields.simple import PasswordField
from wtforms.validators import DataRequired, EqualTo, Required	

class formRegister(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Required('Introduce tu nombre')])
    lastname = StringField('Apellidos', validators=[DataRequired(), Required('Ingrese sus apellidos')])
    documentType = SelectField('Tipo de documento', choices=[('Cédula de Ciudadanía'),('Targeta de Identidad'), ('Pasaporte'), ('Licencia de Conducir')])
    documentNumber = IntegerField('Número de documento', validator=[DataRequired(), Required('Introduzca su número de documento')])
    email = EmailField('Correo', validators=[DataRequired(), validators.Email('Ingrese su correo electónico')])
    age = IntegerField('Edad', validators=[DataRequired(), Required('Ingrese su edad')])
    gender = SelectField('Genero', choices=[('Hombre'), ('Mujer')])
    password = PasswordField('Contraseña', validators=[DataRequired(), Required('Ingrese una contraseña')])
    rePassword = PasswordField('Reafirmar Contraseña', validators=[DataRequired(), EqualTo('password', message='Las contraseñas no coinciden')])
    submit = SubmitField('Continuar')