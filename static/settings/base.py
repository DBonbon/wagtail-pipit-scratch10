# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from typing import Optional

from pipit.env_utils import get_env, get_env_bool  # NOQA: F401

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#BASE_DIR = os.path.dirname(PROJECT_DIR)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Version, be sure to bump this with each release (please follow semver.org)
APP_VERSION = "0.1.0"

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = get_env("SECRET_KEY", required=True)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# This is when debug is off, else django wont allow you to visit the site
#ALLOWED_HOSTS = get_env("ALLOWED_HOSTS", required=True).split(",")

INTERNAL_IPS = ["127.0.0.1"]
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    #"django.contrib.gis",
    # Third party apps
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.admin",
    "wagtail.search",
    "wagtail",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.contrib.modeladmin",
    "wagtail.contrib.routable_page",
    "wagtail.contrib.settings",
    "modelcluster",
    "taggit",
    "wagtail_meta_preview",
    "wagtail_headless_preview",
    "rest_framework",
    # Project specific apps
    "pipit",
    "sitesettings",
    "customuser",
    "customimage",
    "customdocument",
    "main",
    "nextjs",

    "corsheaders",
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]

ROOT_URLCONF = "pipit.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(PROJECT_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "pipit.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dbcards',
        'USER': 'leauser',
        'PASSWORD': 'leauserpsw',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/
TIME_ZONE = "Europe/Stockholm"
LANGUAGE_CODE = "en-us"
SITE_ID = 1
USE_I18N = True
USE_TZ = True
LOCALE_PATHS = [os.path.join(BASE_DIR, "locale")]

# Email
DEFAULT_FROM_EMAIL = get_env("DEFAULT_FROM_EMAIL", default="noreply@example.com")

# Auth
AUTH_USER_MODEL = "customuser.User"

# Wagtail
WAGTAIL_SITE_NAME = "Company-Project"
#WAGTAIL_SITE_NAME = "pipit"
WAGTAILIMAGES_IMAGE_MODEL = "customimage.CustomImage"
WAGTAILDOCS_DOCUMENT_MODEL = "customdocument.CustomDocument"
WAGTAIL_ALLOW_UNICODE_SLUGS = False

WAGTAILSEARCH_BACKENDS = {
    "default": {
        "BACKEND": "wagtail.search.backends.database",
    }
}

WAGTAILIMAGES_FORMAT_CONVERSIONS = {
    "png": "jpeg",
    "webp": "webp",
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# This setting defines the additional locations the staticfiles will traverse
STATICFILES_DIRS = (
    'C:/Users/anica/PycharmProjects/digitalocean-deploy-tests/wagtail-pipit-scratch9/Acme-Blog/src/pipit',
    # "/home/special.polls.com/polls/static",
    # "/home/polls.com/polls/static",
)

# ManifestStaticFilesStorage is recommended in production, to prevent outdated
# JavaScript / CSS assets being served from cache (e.g. after a Wagtail upgrade).
# See https://docs.djangoproject.com/en/4.2/ref/contrib/staticfiles/#manifeststaticfilesstorage
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"



# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
WAGTAILADMIN_BASE_URL = "http://example.com"
