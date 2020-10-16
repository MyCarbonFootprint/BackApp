import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    if 'DATABASE_URI' in os.environ:
        SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URI']


class DevelopmentConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    if 'DATABASE_URI' in os.environ:
        SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URI']


class TestConfig(Config):
    TESTING = True
