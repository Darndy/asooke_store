from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = 'b9cdd0ca2146370d2fe6998e'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Import your models here
from ajkmarket.adbms import User, Item

# Import routes after models and app/db initialization
from ajkmarket import route

