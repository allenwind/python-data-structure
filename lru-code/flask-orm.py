from flask_sqlalchemy import SQLAlchemy
from flask import Flask

class Config:
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost:3306/flask"

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return "<User {}>".format(self.username)

def test():
    db.drop_all()
    db.create_all()
