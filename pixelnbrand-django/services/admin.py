# services/admin.py
from django.contrib import admin
from django.utils.html import mark_safe
from django.utils.text import Truncator
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon_preview', 'is_featured', 'is_active', 'display_order', 'updated_at')
    list_editable = ('display_order', 'is_featured', 'is_active')
    list_filter = ('is_featured', 'is_active', 'created_at')
    search_fields = ('title', 'short_description', 'description', 'content')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at', 'updated_at', 'icon_preview_large', 'featured_image_preview')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'display_order', 'is_featured', 'is_active')
        }),
        ('Content', {
            'fields': (
                'short_description',
                'description',
                'content',
                'featured_image',
                'featured_image_preview',
            ),
            'classes': ('wide',),
        }),
        ('Icon/Image', {
            'fields': ('icon_image', 'icon_preview_large', 'icon'),
            'description': 'Upload an image icon OR use Font Awesome class'
        }),
        ('SEO Settings', {
            'fields': ('meta_title', 'meta_description'),
            'classes': ('collapse',),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    
    def icon_preview(self, obj):
        """Show icon preview in list view"""
        if obj.icon_image:
            return mark_safe(f'<img src="{obj.icon_image.url}" style="max-height: 30px; width: auto;" />')
        elif obj.icon:
            return mark_safe(f'<i class="{obj.icon}" style="font-size: 20px;"></i>')
        return "No icon"
    icon_preview.short_description = 'Icon'
    
    def icon_preview_large(self, obj):
        """Show larger icon preview in edit view"""
        if obj.icon_image:
            return mark_safe(
                f'<div style="margin-top: 10px;">'
                f'<strong>Current Icon:</strong><br>'
                f'<img src="{obj.icon_image.url}" style="max-height: 100px; max-width: 100px; '
                f'border: 1px solid #ddd; padding: 10px; background: white;" />'
                f'</div>'
            )
        return "No image uploaded. You can upload one above or use a Font Awesome icon."
    icon_preview_large.short_description = 'Icon Preview'
    
    def featured_image_preview(self, obj):
        """Show featured image preview"""
        if obj.featured_image:
            return mark_safe(
                f'<div style="margin-top: 10px;">'
                f'<strong>Current Featured Image:</strong><br>'
                f'<img src="{obj.featured_image.url}" style="max-height: 150px; max-width: 300px; '
                f'border: 1px solid #ddd; padding: 10px; background: white;" />'
                f'</div>'
            )
        return "No featured image uploaded."
    featured_image_preview.short_description = 'Featured Image Preview'
    
    def get_queryset(self, request):
        return super().get_queryset(request).order_by('display_order', 'title')
    
    # Custom form for better organization
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['short_description'].widget.attrs['rows'] = 3
        form.base_fields['short_description'].widget.attrs['placeholder'] = 'Brief description (max 150 characters)'
        return form