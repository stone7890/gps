import os

class BaseConfig(object):
  BASE_DIR = os.path.abspath(os.path.dirname(__file__))
  SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost/gps?charset=utf8'
  DATABASE_CONNECT_OPTIONS = {'charset': 'utf8'}
  DEBUG = True
  SQLALCHEMY_TRACK_MODIFICATIONS = True

class DevelopmentConfig(BaseConfig):
  # Define the database
  #SQLALCHEMY_DATABASE_URI= 'mysql://autonomous:binh12345@dbservices.cjuq6wcdcnab.us-east-1.rds.amazonaws.com/autonomous_upgrade'
  SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost/gps?charset=utf8'

class ProductionConfig(BaseConfig):
  DEBUG = False
  # Define the database
  SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@localhost/gps?charset=utf8'
