# portfolio_project/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # As per security best practices, use a non-standard admin URL
    path('secret-admin/', admin.site.urls),

    # Delegate all other URLs to the 'gallery' app's urls.py
    path('', include('gallery.urls')),
]

# This is a crucial step for development ONLY.
# It tells Django's development server how to serve user-uploaded media files.
# In production, Nginx will handle this.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
