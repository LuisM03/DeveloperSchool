import os


SQDU = "sqlite:///database.db"

class Config(object):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "Thismustbesecret"

class productionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = SQDU
    SECRET_KEY = os.environ["SECRET_KEY"]

class developmentConfig(Config):
    DEBUG = True