from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app.routes.home import page_home
from app.routes.formRegisterandLogin import formRegisterandLogin
from app.routes.platform import platform


app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")

db = SQLAlchemy(app)
mg = Migrate(app, db)

# Register blurprints
app.register_blueprint(page_home)
app.register_blueprint(formRegisterandLogin)
app.register_blueprint(platform)


# importamos las rutas
from app.routes import *