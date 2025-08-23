# portfolio_project/settings/production.py
from .base import *

# Production-specific settings
# These values would be set in the production server's environment, not in a .env file
DEBUG = False
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['your-domain.com'])

# --- Security Settings (IMPORTANT!) ---
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# --- CORS for Production ---
# Only allow your frontend domain to access the API
CORS_ALLOWED_ORIGINS = [
    "https://your-domain.com",
    "https://www.your-domain.com",
]
