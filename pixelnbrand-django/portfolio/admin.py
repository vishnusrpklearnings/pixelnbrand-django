# portfolio/admin.py
from django.contrib import admin
from .models import PortfolioItem

@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'client_name', 'is_featured', 'display_order')
    list_filter = ('category', 'is_featured', 'created_at')
    search_fields = ('title', 'description', 'client_name')
    prepopulated_fields = {'slug': ('title',)}
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'description', 'detailed_description', 'category')
        }),
        ('Project Details', {
            'fields': ('client_name', 'project_date', 'project_url', 'technologies')
        }),
        ('Images', {
            'fields': ('image', 'image_2', 'image_3')
        }),
        ('Settings', {
            'fields': ('is_featured', 'display_order')
        }),
    )