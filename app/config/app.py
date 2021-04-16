# http://flask.pocoo.org/docs/1.0/config/
import os


class BaseConfig(object):
    """"
    Base config class
    """
    DEBUG = True
    TESTING = False
    FLASK_ENV = os.getenv('FLASK_ENV')
    CONF_URL = os.getenv('CONF_URL')
    SECRET_KEY = os.getenv('SECRET')


class ProductionConfig(BaseConfig):
    """
    Production specific config
    """
    DEBUG = False
    TESTING = False
    FLASK_ENV = 'production'


class DevelopmentConfig(BaseConfig):
    """"
    Development environment specific configuration
    """
    DEBUG = True
    TESTING = True
    FLASK_ENV = 'development'
