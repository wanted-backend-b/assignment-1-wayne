from .base import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "wayne",
        "USER": "user",
        "PASSWORD": "user",
        "HOST": "mysql",
        "PORT": "3306",
    }
}