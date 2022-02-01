import os


class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    username = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')
    host = os.getenv('HOST')
    port = os.getenv('PORT')
    dbname = os.getenv('DBNAME')
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{dbname}'

