import os

base_path = os.path.dirname(os.path.abspath(__file__))


class Config:
    """Parent configuration class."""

    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///shopyo.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)
    BASE_DIR = base_path
    STATIC = os.path.join(BASE_DIR, "static")
    UPLOADED_PATH_IMAGE = os.path.join(STATIC, "uploads", "images")
    UPLOADED_PATH_THUM = os.path.join(STATIC, "uploads", "thumbs")

    UPLOADED_PRODUCTPHOTOS_DEST = os.path.join(STATIC, "uploads", "products")
    UPLOADED_CATEGORYPHOTOS_DEST = os.path.join(STATIC, "uploads", "category")
    UPLOADED_SUBCATEGORYPHOTOS_DEST = os.path.join(
        STATIC, "uploads", "subcategory"
    )
    PASSWORD_SALT = "abcdefghi"
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{username}:{password}@{server_name}/{db_name}".format(
    #     username='shopyo_user',
    #     password='pass',
    #     server_name='localhost',
    #     db_name='shopyodb'
    # )


class DevelopmentConfig(Config):
    """Configurations for development"""

    ENV = "development"
    DEBUG = True
    LOGIN_DISABLED = False
    # control email confirmation for user registration
    EMAIL_CONFIRMATION_DISABLED = False
    # flask-mailman configs
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = os.environ.get("MAIL_DEFAULT_SENDER")


class TestingConfig(Config):
    """Configurations for testsing"""
    ENV = "testing"
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///testing.db"
    DEBUG = True
    LIVESERVER_PORT = 8943
    LIVESERVER_TIMEOUT = 10
    SERVER_NAME = "localhost.com"
    BCRYPT_LOG_ROUNDS = 4
    WTF_CSRF_ENABLED = False
    # control email confirmation for user registration
    EMAIL_CONFIRMATION_DISABLED = False
    # flask-mailman configs
    MAIL_BACKEND = "console"
    MAIL_USERNAME = "shopyofrom@test.com"
    MAIL_PASSWORD = "pass"
    MAIL_DEFAULT_SENDER = "shopyofrom@test.com"


app_config = {
    "development": DevelopmentConfig,
    "production": Config,
    "testing": TestingConfig,
}
