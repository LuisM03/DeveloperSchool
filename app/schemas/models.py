from app import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30))
    lastname = db.Column(db.String(60))
    documentType = db.Column(db.String(30), unique = True)
    documentNumber = db.Column(db.Integer, unique = True)
    age = db.Column(db.Integer)
    email = db.Column(db.String(60))
    password = db.Column(db.String(60))
    gender = db.Column(db.String(30))

    def __init__(self, name, lastname, documentType, documentNumber, age, email, password, gender):
        self.name = name
        self.lastname = lastname
        self.documentType = documentType
        self.documentNumber = documentNumber
        self.age = age
        self.email = email
        self.password = password
        self.gender = gender


    def __repr__(self) -> str:
        return '<User %r>' %self.name