# portfolio_project/settings/production.py
from .base import *

# Production-specific settings
# These values would be set in the production server's environment, not in a .env file
SECRET_KEY = env('SECRET_KEY')
DEBUG = False
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')
#ALLOWED_HOSTS = ['portfolio.inaneprojects.online']
# --- Security Settings (IMPORTANT!) ---
# These settings are crucial for a production environment.

# Redirects all HTTP requests to HTTPS.
SECURE_SSL_REDIRECT = True

# Tells Django to trust the X-Forwarded-Proto header from our proxy (Nginx).
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Helps prevent XSS attacks by enabling the browser's XSS filter.
SECURE_BROWSER_XSS_FILTER = True

# Prevents the browser from guessing the content type of a file, which can prevent certain attacks.
SECURE_CONTENT_TYPE_NOSNIFF = True

# Enables HTTP Strict Transport Security (HSTS).
# This tells the browser to only communicate with your site over HTTPS for the next year.
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True # Submit your site to browser HSTS preload lists

# Ensures that the session cookie is only sent over a secure (HTTPS) connection.
SESSION_COOKIE_SECURE = True

# Ensures that the CSRF cookie is only sent over a secure (HTTPS) connection.
CSRF_COOKIE_SECURE = True

# --- Database Configuration for PostgreSQL ---
# The DATABASE_URL will be set on the server like:
# DATABASE_URL=postgres://user:password@host:port/dbname
DATABASES = {
    'default': env.db(),
}

# --- Static Files with WhiteNoise ---
# WhiteNoise allows your web app to serve its own static files without
# relying on Nginx or a separate CDN. It's highly efficient.
# Add 'whitenoise.middleware.WhiteNoiseMiddleware' to the top of your MIDDLEWARE list in base.py
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# --- Logging Configuration ---
# This sends error logs to the console, which will be captured by the systemd journal.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING', # Change to INFO for more verbose logs
    },
}

