import os


class Config:
    """
    Set default config values here
    e.g. CONFIG_VALUE = os.environ.get('CONFIG_VALUE_ENV_VAR') or 'default value'
    """
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
    DEBUG = True


class TestConfig(Config):
    """
    Set test specific config here
    """
    TESTING = True


class ProdConfig(Config):
    """
    Set prod specific config here
    """

config = {
    "dev": DevConfig,
    "test": TestConfig,
    "prod": ProdConfig,
    "default": ProdConfig,
}
