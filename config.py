import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = '0d34c570fe907877d19a69275de527e076bf31f688c1a171d38ba24169512bed'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

"""
postgres://bfjihmhtoehdts:0d34c570fe907877d19a69275de527e076bf31f688c1a171d38ba24169512bed@ec2-3-214-3-162.compute-1.amazonaws.com:5432/d3kvj8id3oipp6
"""
class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True