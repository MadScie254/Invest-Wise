import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = "your_secret_key"

DEBUG = True  # Set to False in production

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "yourdomain.com"]

# Database Configuration
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

# Static Files Configuration
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Media Files Configuration
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Time Zone Setting
TIME_ZONE = "Africa/Nairobi"

# Email Configuration
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Authentication Configuration
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
    "allauth.socialaccount.providers.google.GoogleOAuth2Provider",
    "allauth.socialaccount.providers.facebook.FacebookOAuth2Provider",
    "allauth.socialaccount.providers.twitter.TwitterOAuth",
    "allauth.socialaccount.providers.linkedin.LinkedinOAuth2Provider",
    "allauth.socialaccount.providers.github.GithubOAuth2Provider",
    "allauth.socialaccount.providers.bitbucket.BitbucketOAuth2Provider",
    "allauth.socialaccount.providers.instagram.InstagramOAuth2Provider",
    "allauth.socialaccount.providers.slack.SlackOAuth2Provider",
    "allauth.socialaccount.providers.gitlab.GitLabOAuth2Provider",
    "allauth.socialaccount.providers.dropbox.DropboxOAuth2Provider",
    "allauth.socialaccount.providers.orcid.OrcidOAuth2Provider",
    "allauth.socialaccount.providers.azuread.AzureADOAuth2",
    "allauth.socialaccount.providers.azuread_b2c.AzureADB2COAuth2",
    "allauth.socialaccount.providers.salesforce.SalesforceOAuth2",
    "allauth.socialaccount.providers.salesforce.SalesforceSandboxOAuth2",
]


# USE_I18N and USE_L10N Settings
USE_I18N = True
USE_L10N = True

# LANGUAGE_CODE Setting
LANGUAGE_CODE = "en-us"  # Set to your desired language code

# TEMPLATES Setting
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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

# MIDDLEWARE Setting
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.contrib.auth.middleware.SessionAuthenticationMiddleware",
]

# INSTALLED_APPS Setting
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "your_app_name",  # Replace with the actual name of your Django app
    # Add other installed apps as needed
]

# ROOT_URLCONF Setting
ROOT_URLCONF = "your_app_name.urls"
# WSGI_APPLICATION Setting
WSGI_APPLICATION = "your_app_name.wsgi.application"
# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
        "ATOMIC_REQUESTS": True,
        "CONN_MAX_AGE": 60,
        "OPTIONS": {
            "timeout": 10000,
            "options": "-c search_path=your_schema",
            "sslmode": "require",
            "sslcert": "path/to/cert.pem",
            "sslkey": "path/to/key.pem",
            "sslrootcert": "path/to/rootcert.pem",
            "sslcrl": "path/to/crl.pem",
            "sslcompression": "1",
            "sslcertdir": "path/to/certdir",
            "sslcrlpath": "path/to/crlpath",
            "sslciphers": "ALL",
            "sslcompression": "1",
            "application_name": "your_app_name",
        },
    }
}


# AUTH_USER_MODEL Setting
AUTH_USER_MODEL = (
    "your_app_name.CustomUser"  # Replace with your custom user model if needed
)

# LOGIN_URL and LOGIN_REDIRECT_URL Settings
LOGIN_URL = "login_user"
LOGIN_REDIRECT_URL = "user_dashboard"

# SECRET_KEY Setting
SECRET_KEY = "your_secret_key"  # Replace with a strong, random secret key

# SECURE_BROWSER_XSS_FILTER and SECURE_CONTENT_TYPE_NOSNIFF Settings
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# SECURE_SSL_REDIRECT Setting
SECURE_SSL_REDIRECT = True

# SECURE_HSTS Setting
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# SESSION_COOKIE_SECURE and CSRF_COOKIE_SECURE Settings
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# SESSION_ENGINE Setting
SESSION_ENGINE = (
    "django.contrib.sessions.backends.db"  # Choose the session engine as needed
)

# CORS_ALLOWED_ORIGINS Setting (if using Django CORS Headers)
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # Example: Add your frontend origin
    # Add other allowed origins as needed
]

# REST_FRAMEWORK Setting (if using Django REST framework)
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}

# LOGGING Setting
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "debug.log",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file"],
            "level": "DEBUG",
            "propagate": True,
        },
    },
}

# DEFAULT_AUTO_FIELD Setting
DEFAULT_AUTO_FIELD = (
    "django.db.models.BigAutoField"  # Choose the default primary key field for models
)

# STATIC_URL and MEDIA_URL Settings
STATIC_URL = "/static/"
MEDIA_URL = "/media/"

# DEFAULT_FILE_STORAGE Setting
DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"  # Specify the default storage backend for media files

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Custom settings
MY_CUSTOM_SETTING = "my_custom_value"
