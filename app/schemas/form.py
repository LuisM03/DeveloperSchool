from flask_wtf import FlaskForm
from wtforms import IntegerField,SelectField,SubmitField,StringField
from wtforms import validators
from wtforms.fields.html5 import EmailField
from wtforms.fields.simple import PasswordField
from wtforms.validators import DataRequired, EqualTo, Required	

class formRegister(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Required('Introduce tu nombre')], render_kw={"placeholder": "Nombre"})
    lastname = StringField('Apellidos', validators=[DataRequired(), Required('Ingrese sus apellidos')], render_kw={"placeholder": "Apellidos"})
    documentType = SelectField('Tipo de documento', choices=[('Cédula de Ciudadanía'),('Targeta de Identidad'), ('Pasaporte'), ('Licencia de Conducir')], render_kw={"placeholder": "Tipo de documento"})
    documentNumber = IntegerField('Número de documento', validators=[DataRequired(), Required('Introduzca su número de documento')], render_kw={"placeholder": "Número de documento"})
    email = EmailField('Correo', validators=[DataRequired(), validators.Email('Ingrese su correo electónico')], render_kw={"placeholder": "Correo"})
    age = IntegerField('Edad', validators=[DataRequired(), Required('Ingrese su edad')], render_kw={"placeholder": "Edad"})
    gender = SelectField('Genero', choices=[('Sexo'), ('Hombre'), ('Mujer')], render_kw={"placeholder": "Sexo"})
    password = PasswordField('Contraseña', validators=[DataRequired(), Required('Ingrese una contraseña')], render_kw={"placeholder": "Contraseña"})
    rePassword = PasswordField('Reafirmar Contraseña', validators=[DataRequired(), EqualTo('password', message='Las contraseñas no coinciden')], render_kw={"placeholder": "Confirmar contraseña"})
    submit = SubmitField('Continuar')