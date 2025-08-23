# gallery/urls.py

from django.urls import path
from . import views # Import the views from the current directory

# This is used for namespacing, but for a single app it's optional. Good practice though.
app_name = 'gallery'

urlpatterns = [
    # Homepage
    path('', views.HomePageView.as_view(), name='home'),

    # Portfolio Pages
    path('portfolio/', views.PortfolioListView.as_view(), name='portfolio_list'),
    path('portfolio/<slug:slug>/', views.PortfolioDetailView.as_view(), name='portfolio_detail'),

    # Blog Pages
    path('blog/', views.BlogListView.as_view(), name='blog_list'),
    path('blog/<slug:slug>/', views.BlogDetailView.as_view(), name='blog_detail'),
]
