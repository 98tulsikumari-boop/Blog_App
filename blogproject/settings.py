import os
from datetime import timedelta, datetime


from pathlib import Path
from dotenv import load_dotenv

# Read .env file
load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-j&b1r+asi%yawx6ia@@n!jnfni*6tt($*(4#&-!=$f-m4jint+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# ---------------Cloudflared Setup------------------------------
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    ".trycloudflare.com",
]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

CSRF_TRUSTED_ORIGINS = [
    "https://*.trycloudflare.com",
]

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
# ---------------------------------------


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # My app
    'app_api_blog.apps.AppApiBlogConfig',
    'app_api_tag.apps.AppApiTagConfig',
    'app_api_category.apps.AppApiCategoryConfig',
    'app_api_account.apps.AppApiAccountConfig',
    'app_api_contact.apps.AppApiContactConfig',
    'app_api_newsletter.apps.AppApiNewsletterConfig',
    'app_api_bookmark.apps.AppApiBookmarkConfig',

    # Third party app
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# CORS Settings
# CORS_ALLOW_ALL_ORIGINS = [
#     "http://localhost:8000",
#     "http://127.0.0.1:8000",
# ]

# ================= CORS CONFIGURATION =================
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
CORS_ALLOW_CREDENTIALS = True

# Critical for fixing 401 Unauthorized during Axios requests
CORS_ALLOW_HEADERS = [
    "accept",
    "authorization",
    "content-type",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]

ROOT_URLCONF = 'blogproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'blogproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Media Files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

AUTH_USER_MODEL = 'app_api_account.User'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES = [os.path.join(BASE_DIR, 'static')]

# Login Url
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'blog_list'
LOGOUT_REDIRECT_URL = 'blog_list'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# JWT Configuration
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=24),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'AUTH_HEADER_TYPES': ('Bearer',),
}

# ================= EMAIL CONFIGURATION =================

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = '98tulsikumari@gmail.com'
EMAIL_HOST_PASSWORD = 'mqad izew ypjd vfoe'


DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


JAZZMIN_SETTINGS = {
    "site_title": "WellBe Admin",
    "site_header": "WellBe Dashboard",
    "site_brand": "WellBe",
    # "site_logo": "images/logo.png",  # optional (match your site logo)
    "login_logo": "images/logo.png",
    "site_logo_classes": "img-circle elevation-1",
    "welcome_sign": "Welcome to WellBe Admin Panel 🌿",

    "search_model": [
        "auth.User",
        "app_api_blog.Blog",
        "app_api_tag.Tag",
    ],

    "changeform_format": "tabs",
    "show_ui_builder": False,

    # CUSTOM CSS (VERY IMPORTANT)
    "custom_css": "css/admin_custom.css",
}


JAZZMIN_UI_TWEAKS = {

    # Text sizing
    "navbar_small_text": False,
    "footer_small_text": True,
    "body_small_text": False,
    "brand_small_text": False,

    # 🌿 BRAND COLORS
    "brand_colour": "navbar-success",
    "accent": "accent-success",

    # NAVBAR
    "navbar": "navbar-success navbar-dark",
    "navbar_fixed": True,
    "no_navbar_border": True,

    # SIDEBAR
    "sidebar": "sidebar-light-success",
    "sidebar_fixed": True,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_flat_style": True,

    # LAYOUT
    "layout_boxed": False,
    "footer_fixed": False,

    # THEME
    "theme": "flatly",      # clean & modern
    "dark_mode_theme": None,

    # BUTTONS (soft wellness colors)
    "button_classes": {
        "primary": "btn-success",
        "secondary": "btn-outline-success",
        "info": "btn-outline-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success",
    }
}
