# portfolio_project/settings/development.py
from .base import *

ALLOWED_HOSTS = ['192.168.29.173']
# In development, we can be more permissive with CORS
CORS_ALLOW_ALL_ORIGINS = True
