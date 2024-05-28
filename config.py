import os
from os.path import join
import json
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY',"DCj5WyH32A7m5tz")
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI','sqlite:///' +join(basedir, 'app.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False

