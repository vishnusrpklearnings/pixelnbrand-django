from django.contrib import admin
from .models import Testimonial

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'company', 'rating', 'is_active', 'display_order')
    list_filter = ('is_active', 'rating')
    search_fields = ('client_name', 'company', 'content')
    list_editable = ('display_order', 'is_active', 'rating')