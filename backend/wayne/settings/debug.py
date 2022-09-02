from .base import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "wayne",
        "USER": "root",
        "PASSWORD": "root1234",
        "HOST": "localhost",
        "PORT": "3306",
    }
}