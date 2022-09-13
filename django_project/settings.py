from pathlib import Path
import environ
import collections

collections.Callable = collections.abc.Callable

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    DEBUG=(bool, False),
    ENVIRONMENT=(str, "PRODUCTION"),
    ALLOW_ALL_ORIGINS=(bool, False),
    ALLOWED_HOSTS=(list, []),
    ALLOWED_ORIGINS=(list, []),
    DATABASE_ENGINE=(str, "django.db.backends.sqlite3"),
    DATABASE_NAME=(str, BASE_DIR / "db.sqlite3"),
    DATABASE_USER=(str, ""),
    DATABASE_PASSWORD=(str, ""),
    DATABASE_HOST=(str, ""),
    DATABASE_PORT=(int, 5432),
)

environ.Env.read_env()

ENVIRONMENT = env.str("ENVIRONMENT")

SECRET_KEY = env.str("SECRET_KEY")

DEBUG = env.bool("DEBUG")

ALLOWED_HOSTS = tuple(env.list("ALLOWED_HOSTS"))

# APPS
# ------------------------------------------------------------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    # Third-party
    "allauth",
    "allauth.account",
    # "crispy_forms",
    # "debug_toolbar",
    "django_countries",
    'rest_framework',
    'corsheaders',
    'drf_yasg',
    'django_nose',

    # Local
    "accounts",
    'campaign',
    "user_campaign_connection",
    'post',
]

# MIDDLEWARE
# ------------------------------------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    # "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# URLS
# ------------------------------------------------------------------------------
ROOT_URLCONF = "django_project.urls"
WSGI_APPLICATION = "django_project.wsgi.application"

# TEMPLATES
# ------------------------------------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

# DATABASES
# ------------------------------------------------------------------------------
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

# For Docker/PostgreSQL usage uncomment this and comment the DATABASES config above
DATABASES = {
    "default": {
        "ENGINE": env.str("DATABASE_ENGINE"),
        "NAME": env.str("DATABASE_NAME"),
        "USER": env.str("DATABASE_USER"),
        "PASSWORD": env.str("DATABASE_PASSWORD"),
        "HOST": env.str("DATABASE_HOST"),
        "PORT": env.int("DATABASE_PORT"),
    }
}

# PASSWORDS
# ------------------------------------------------------------------------------
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

# INTERNATIONALIZATION
# ------------------------------------------------------------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True


# # STATIC

STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_URL = "/static/"
# STATICFILES_DIRS = BASE_DIR / "staticfiles"
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# DJANGO-CRISPY-FORMS CONFIGS
# ------------------------------------------------------------------------------
CRISPY_TEMPLATE_PACK = "bootstrap4"

# EMAIL
# ------------------------------------------------------------------------------
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# DJANGO-DEBUG-TOOLBAR CONFIGS
# ------------------------------------------------------------------------------
INTERNAL_IPS = ["127.0.0.1"]

# CUSTOM USER MODEL CONFIGS
# ------------------------------------------------------------------------------
AUTH_USER_MODEL = "accounts.CustomUser"

# Use nose to run all tests
# TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# NOSE_ARGS = [
#     '--with-coverage',
#     '--cover-package=accounts, campaign, post, user_campaign_connection',
#     '--cover-html',
# ]

# DJANGO-ALLAUTH CONFIGS
# ------------------------------------------------------------------------------
SITE_ID = 1
LOGIN_REDIRECT_URL = "home"
ACCOUNT_LOGOUT_REDIRECT_URL = "home"
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True



# added here 
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ],
}

CORS_ORIGIN_WHITELIST = tuple(env.list("ALLOWED_ORIGINS"))
CORS_ALLOW_ALL_ORIGINS = env.bool("ALLOW_ALL_ORIGINS")
CSRF_TRUSTED_ORIGINS = tuple(env.list("ALLOWED_ORIGINS"))
CORS_ALLOWED_ORIGINS = tuple(env.list("ALLOWED_ORIGINS"))

