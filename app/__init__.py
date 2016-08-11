from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('configs.DevelopmentConfig')
#app.config.from_object('configs.ProductionConfig')

db = SQLAlchemy(app)

from app import controllers


