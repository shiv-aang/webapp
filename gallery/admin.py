from django.contrib import admin
from .models import PortfolioItem, BlogPost
from django.utils.html import format_html

@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_featured', 'created_date', 'image_preview')
    list_filter = ('is_featured', 'technologies_used')
    search_fields = ('title', 'description', 'technologies_used')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('image_preview_detail',)

    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'technologies_used')
        }),
        ('Media', {
            'fields': ('image', 'image_preview_detail')
        }),
        ('Links', {
            'fields': ('project_url', 'github_url')
        }),
        ('Advanced Options', {
            'classes': ('collapse',),
            'fields': ('is_featured', 'meta_description'),
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return "No Image"
    image_preview.short_description = 'Image'

    def image_preview_detail(self, obj):
        return self.image_preview(obj)
    image_preview_detail.short_description = 'Current Image'


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_published', 'publish_date', 'read_time_minutes')
    list_filter = ('is_published', 'author')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('read_time_minutes', 'created_date', 'updated_date')
    actions = ['publish_posts', 'unpublish_posts']

    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'author', 'content', 'excerpt')
        }),
        ('Media & Metadata', {
            'fields': ('featured_image', 'tags')
        }),
        ('Publishing', {
            'fields': ('is_published', 'publish_date')
        }),
        ('SEO', {
            'classes': ('collapse',),
            'fields': ('meta_description',),
        }),
        ('Auto-Generated Fields', {
            'classes': ('collapse',),
            'fields': ('read_time_minutes', 'created_date', 'updated_date'),
        }),
    )

    def publish_posts(self, request, queryset):
        queryset.update(is_published=True)
    publish_posts.short_description = "Mark selected posts as published"

    def unpublish_posts(self, request, queryset):
        queryset.update(is_published=False)
    unpublish_posts.short_description = "Mark selected posts as unpublished"
