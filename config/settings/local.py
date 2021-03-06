import os

from .base import *  # noqa
from .base import ROOT_DIR, TEMPLATES, env


# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True
# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES[-1]["APP_DIRS"] = True
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY",
    default="kY2h68D0TgYGFibh1GiRlZ1PLE52zTKpbIFIymEsNc5zoauSn6asnnSr2dtOiOf1",
)
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

# CACHES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = os.getenv(
    "DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend"
)
EMAIL_HOST = "localhost"
EMAIL_PORT = 1025

# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
# In docker use postgres otherwise use sqlite3
if os.getenv("USE_DOCKER") == "yes":
    DATABASES = {"default": env.db("DATABASE_URL")}
    DATABASES["default"]["ATOMIC_REQUESTS"] = True
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(ROOT_DIR, "db.sqlite3"),
        }
    }
