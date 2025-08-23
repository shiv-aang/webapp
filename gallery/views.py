# gallery/views.py

from django.views.generic import TemplateView, ListView, DetailView
from .models import PortfolioItem, BlogPost

class HomePageView(TemplateView):
    """
    View for the homepage.
    """
    template_name = "gallery/index.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in QuerySets of featured portfolio items and recent blog posts
        context['featured_portfolio_items'] = PortfolioItem.objects.filter(is_featured=True).order_by('-created_date')[:3]
        context['recent_blog_posts'] = BlogPost.objects.filter(is_published=True).order_by('-publish_date')[:3]
        return context

class PortfolioListView(ListView):
    """
    View to display a list of all portfolio items.
    """
    model = PortfolioItem
    template_name = 'gallery/portfolio_list.html'
    context_object_name = 'portfolio_items' # Name to use in the template loop
    paginate_by = 9 # Show 9 items per page
    queryset = PortfolioItem.objects.order_by('-created_date') # Order by newest first

class PortfolioDetailView(DetailView):
    """
    View to display a single portfolio item.
    """
    model = PortfolioItem
    template_name = 'gallery/portfolio_detail.html'
    # Django automatically uses the slug from the URL to fetch the correct item.

class BlogListView(ListView):
    """
    View to display a list of published blog posts.
    """
    model = BlogPost
    template_name = 'gallery/blog_list.html'
    context_object_name = 'blog_posts'
    paginate_by = 5
    # We only want to show posts that are marked as published
    queryset = BlogPost.objects.filter(is_published=True).order_by('-publish_date')

class BlogDetailView(DetailView):
    """
    View to display a single blog post.
    """
    model = BlogPost
    template_name = 'gallery/blog_detail.html'
