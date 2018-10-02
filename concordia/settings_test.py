from .settings_template import *

LOGGING["handlers"]["stream"]["level"] = "INFO"
LOGGING["handlers"]["file"]["level"] = "INFO"
LOGGING["handlers"]["file"]["filename"] = "./logs/concordia-web.log"
LOGGING["handlers"]["celery"]["level"] = "INFO"
LOGGING["handlers"]["celery"]["filename"] = "./logs/concordia-celery.log"
LOGGING["loggers"]["django"]["level"] = "INFO"
LOGGING["loggers"]["celery"]["level"] = "INFO"

DEBUG = False

DATABASES["default"] = {
    "ENGINE": "django.db.backends.sqlite3",
    "NAME": "concordia-tests",
}

# If you're running a docker db container, use this:
# DATABASES["default"]["PORT"] = "54323"

DEFAULT_TO_EMAIL = "rstorey@loc.gov"

ALLOWED_HOSTS = ["127.0.0.1", "0.0.0.0"]

CONCORDIA = {"netloc": "http://0.0.0.0:8000"}

EMAIL_BACKEND = "django.core.mail.backends.dummy.EmailBackend"
