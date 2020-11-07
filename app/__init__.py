# app/__init__.py
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Loading Flask
app = Flask(__name__)
# Loading config.py
app.config.from_object(Config)
# Defining database
db = SQLAlchemy(app)
# Setting up migration between app and database
migrate = Migrate(app, db)

# Importing routes and models
from app import routes, models, forms
