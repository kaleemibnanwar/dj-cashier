# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

import django

DEBUG = True
USE_TZ = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "^9-s9xk=xm73x!up_))lw0sl!!z1k^gqo+y$d3))xiv)7zni&-"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

ROOT_URLCONF = "tests.urls"

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "dj_cashier.apps.DjCashierConfig",
]

SITE_ID = 1

if django.VERSION >= (1, 10):
    MIDDLEWARE = ()
else:
    MIDDLEWARE_CLASSES = ()
