from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import math

class PortfolioItem(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, help_text="Auto-generated from title. Used for SEO-friendly URLs.")
    description = models.TextField()
    technologies_used = models.CharField(max_length=200, help_text="Comma-separated tech stack")
    image = models.ImageField(upload_to='portfolio_images/%Y/%m/')
    project_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    is_featured = models.BooleanField(default=False, help_text="Feature this item on the homepage.")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    meta_description = models.CharField(max_length=160, blank=True, help_text="Brief description for SEO (max 160 characters).")

    def save(self, *args, **kwargs):
        # If the slug is not set, create it from the title
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, help_text="Auto-generated from title.")
    content = models.TextField(help_text="Main content of the blog post. Rich text support can be added later.")
    excerpt = models.TextField(blank=True, help_text="A short summary for list views.")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    featured_image = models.ImageField(upload_to='blog_images/%Y/%m/')
    tags = models.CharField(max_length=200, blank=True, help_text="Comma-separated tags.")
    is_published = models.BooleanField(default=False)
    publish_date = models.DateTimeField(help_text="The date the post will be considered published.")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    meta_description = models.CharField(max_length=160, blank=True, help_text="Brief description for SEO (max 160 characters).")
    read_time_minutes = models.PositiveIntegerField(blank=True, null=True, help_text="Calculated automatically on save.")

    def save(self, *args, **kwargs):
        # Auto-generate slug
        if not self.slug:
            self.slug = slugify(self.title)

        # Calculate read time (average reading speed is ~200-250 words per minute)
        word_count = len(self.content.split())
        self.read_time_minutes = math.ceil(word_count / 225)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
