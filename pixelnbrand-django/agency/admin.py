# agency/admin.py
from django.contrib import admin
from django.utils.html import mark_safe
from .models import SiteSettings

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    """Admin for site settings with all homepage fields"""
    
    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    fieldsets = (
        ('Company Information', {
            'fields': (
                'company_name',
                'logo',
                'logo_preview',
                'logo_alt_text',
                'show_logo_only',
                'tagline',
            ),
        }),
        ('Homepage - Hero Section', {
            'fields': (
                'hero_title',
                'hero_description',
                'hero_button_text',
                'hero_image',
                'hero_image_preview',
            ),
        }),
        ('Homepage - Services Section', {
            'fields': ('services_title', 'services_description'),
        }),
        ('Homepage - Testimonials Section', {
            'fields': ('testimonials_title', 'testimonials_description'),
        }),
        ('Homepage - Portfolio Section', {
            'fields': ('portfolio_title', 'portfolio_description'),
        }),
        ('Homepage - CTA Section', {
            'fields': ('cta_title', 'cta_description', 'cta_button_text'),
        }),
        ('Contact Information', {
            'fields': ('contact_phone', 'contact_email', 'company_address'),
        }),
    )
    
    readonly_fields = ('logo_preview', 'hero_image_preview')
    
    def logo_preview(self, obj):
        if obj and obj.logo:
            return mark_safe(f'<img src="{obj.logo.url}" style="max-height: 50px;" />')
        return "No logo uploaded"
    logo_preview.short_description = 'Current Logo'
    
    def hero_image_preview(self, obj):
        if obj and obj.hero_image:
            return mark_safe(f'<img src="{obj.hero_image.url}" style="max-height: 100px;" />')
        return "No hero image uploaded"
    hero_image_preview.short_description = 'Current Hero Image'
    
    def changelist_view(self, request, extra_context=None):
        from django.shortcuts import redirect
        from django.urls import reverse
        
        obj, created = SiteSettings.objects.get_or_create(pk=1)
        return redirect(
            reverse('admin:%s_%s_change' % (
                self.model._meta.app_label,
                self.model._meta.model_name
            ), args=[obj.pk])
        )