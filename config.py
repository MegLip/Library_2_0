# config.py
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
   SECRET_KEY = os.environ.get("SECRET_KEY") or "welcome to the jungle"
   SQLALCHEMY_DATABASE_URI = (
           os.environ.get('DATABASE_URL') or
           'sqlite:///' + os.path.join(BASE_DIR, 'library.db')
   )
   SQLALCHEMY_TRACK_MODIFICATIONS = False
