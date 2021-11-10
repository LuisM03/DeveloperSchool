from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object("config.developmentConfig")

db = SQLAlchemy(app)
mg = Migrate(app, db)


# importamos las rutas
from app.routes import *