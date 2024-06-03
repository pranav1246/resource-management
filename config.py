class Config(object):
    DEBUG= False
    TESTING=False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI='sqlite:///dev.db'
    SECRET_KEY = 'thisissecretkey'
    SECURITY_PASSWORD_SALT = 'thisissalt'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False
    SECURITY_TOKEN_AUTHENTICATION_HEADER = 'aunthentication-token'


