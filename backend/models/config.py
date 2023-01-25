import os
from datetime import datetime, timedelta, timezone

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', '123')
DB_HOST = os.getenv('DB_HOST', 'localhost:5432')
DB_NAME = os.getenv('DB_NAME', 'edu_system')
database_path = 'postgresql://{}:{}@{}/{}'.format(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)
SEND_FILE_MAX_AGE_DEFAULT = timedelta(hours=12)
SQLALCHEMY_DATABASE_URI = database_path
SQLALCHEMY_TRACK_MODIFICATIONS = False
TEMPLATES_AUTO_RELOAD = True
SQLALCHEMY_ECO = True
MAX_CONTENT_LENGTH = 15 * 1000 * 1000
JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
JWT_SECRET_KEY = "edu_system"
JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
FLASK_ENV = "development"
FLASK_DEBUG = 1
