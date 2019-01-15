""" import operating system"""
import os


class Config(object):
    """
        Parent configuration class
    """
    DEBUG = False


class DevelopmentConfig(Config):
    """
        Configuratins for Development Production environment
    """
    DEVELOPMENT = True
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    """
        Configurations for Production environment
    """
    DEBUG = False
    TESTING = False

class TestingConfig(Config):
    """
        Configurations for testing environment
    """
    TESTING = True
    DEBUG = True
    os.environ['ENV'] = 'testing'


app_config = {
    'development' : DevelopmentConfig,
    'testing' : TestingConfig,
    'production' : ProductionConfig
}
