# services/views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from agency.models import SiteSettings
from .models import Service

def service_list(request):
    """List all active services"""
    services = Service.objects.filter(is_active=True).order_by('display_order')
    site_settings = SiteSettings.load()
    
    context = {
        'services': services,
        'site_settings': site_settings,
    }
    return render(request, 'services/list.html', context)

def service_detail(request, slug):
    """Show individual service detail page"""
    service = get_object_or_404(Service, slug=slug, is_active=True)
    site_settings = SiteSettings.load()
    
    # Get related services (exclude current one)
    related_services = Service.objects.filter(
        is_active=True
    ).exclude(
        id=service.id
    ).order_by('display_order')[:3]
    
    context = {
        'service': service,
        'related_services': related_services,
        'site_settings': site_settings,
    }
    # CHANGE THIS LINE:
    return render(request, 'services/details.html', context)
 