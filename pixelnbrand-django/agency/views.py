# agency/views.py - UPDATED VERSION
from django.shortcuts import render
from services.models import Service
from portfolio.models import PortfolioItem
from testimonials.models import Testimonial
from agency.models import SiteSettings

def home(request):
    # Get services for homepage (limit to 6)
    services = Service.objects.filter(is_active=True).order_by('display_order')[:6]
    
    # Get total services count for "More Services" button
    total_services = Service.objects.filter(is_active=True).count()
    
    testimonials = Testimonial.objects.filter(is_active=True).order_by('display_order')
    portfolio_items = PortfolioItem.objects.filter(is_featured=True).order_by('display_order')[:6]
    
    # Get site settings
    site_settings = SiteSettings.load()
    
    context = {
        'services': services,
        'total_services': total_services,  # Pass total count
        'testimonials': testimonials,
        'portfolio_items': portfolio_items,
        'site_settings': site_settings,
        
        # Pass all homepage fields
        'hero_title': site_settings.hero_title,
        'hero_description': site_settings.hero_description,
        'hero_button_text': site_settings.hero_button_text,
        
        'services_title': site_settings.services_title,
        'services_description': site_settings.services_description,
        
        'testimonials_title': site_settings.testimonials_title,
        'testimonials_description': site_settings.testimonials_description,
        
        'portfolio_title': site_settings.portfolio_title,
        'portfolio_description': site_settings.portfolio_description,
        
        'cta_title': site_settings.cta_title,
        'cta_description': site_settings.cta_description,
        'cta_button_text': site_settings.cta_button_text,
    }
    return render(request, 'home/index.html', context)

def about(request):
    site_settings = SiteSettings.load()
    context = {
        'site_settings': site_settings,
    }
    return render(request, 'home/about.html', context)