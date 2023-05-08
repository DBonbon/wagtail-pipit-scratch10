"""
Write prod settings here, or override base settings
"""
import sentry_sdk
from sentry_sdk import configure_scope
from sentry_sdk.integrations.django import DjangoIntegration

from .local import *  # NOQA


DEBUG = False

DATABASES["default"]["CONN_MAX_AGE"] = int(
    get_env("DATABASE_CONN_MAX_AGE", default="60")
)

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "cache_table",
    },
    "renditions": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "cache_table_rendition",
        "TIMEOUT": 600,
        "OPTIONS": {
            "MAX_ENTRIES": 1000,
        },
    },
}

"""STATICFILES_STORAGE = (
    "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"  # NOQA
)"""
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

COMPRESS_OFFLINE = True
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]
COMPRESS_CSS_HASHING_METHOD = 'content'

# Enable caching of templates in production environment
TEMPLATES[0]["OPTIONS"]["loaders"] = [  # type: ignore[index]
    (
        "django.template.loaders.cached.Loader",
        [
            "django.template.loaders.filesystem.Loader",
            "django.template.loaders.app_directories.Loader",
        ],
    )
]

# This ensures that Django will be able to detect a secure connection
# properly on Heroku.
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Prevent Man in the middle attacks with HTTP Strict Transport Security
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# Block content that appears to be an XSS attack in certain browsers
SECURE_BROWSER_XSS_FILTER = True

# Use a secure cookie for the session cookie
SESSION_COOKIE_SECURE = True

# Use a secure cookie for the CSRF cookie
CSRF_COOKIE_SECURE = True

# Email notification url
WAGTAILADMIN_BASE_URL = "https://blog.acme.com"

# Sentry
SENTRY_DSN = get_env("SENTRY_DSN", required=False)
SENTRY_ENVIRONMENT = "prod"

sentry_sdk.init(
    dsn=SENTRY_DSN,
    release=APP_VERSION,
    environment=SENTRY_ENVIRONMENT,
    integrations=[DjangoIntegration()],
)

# Add sentry to logging
with configure_scope() as scope:
    scope.level = "error"
