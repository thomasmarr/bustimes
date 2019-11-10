import os


class Config:
    """
    Set default config values here
    e.g. CONFIG_VALUE = os.environ.get('CONFIG_VALUE_ENV_VAR') or 'default value'
    """
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY")
    TFL_APP_ID = os.environ.get("TFL_APP_ID")
    TFL_API_KEY = os.environ.get("TFL_API_KEY")
    MONGODB_SETTINGS = {
        'db': os.environ.get('MONGO_INITDB_DATABASE'),
        'host': os.environ.get('MONGODB_HOST'),
        'username': os.environ.get('MONGO_INITDB_USERNAME'),
        'password': os.environ.get('MONGO_INITDB_PASSWORD')
    }



class DevConfig(Config):
    """
    Set dev specific config here
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URL")
    DEBUG = True


class TestConfig(Config):
    """
    Set test specific config here
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get("TEST_DATABASE_URL")
    TESTING = True


class ProdConfig(Config):
    """
    Set prod specific config here
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get("PROD_DATABASE_URL")

config = {
    "dev": DevConfig,
    "test": TestConfig,
    "prod": ProdConfig,
    "default": ProdConfig,
}
