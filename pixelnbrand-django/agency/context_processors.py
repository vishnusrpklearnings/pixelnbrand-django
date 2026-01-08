# agency/context_processors.py - CORRECTED VERSION
from .models import SiteSettings  # Changed from SiteSetting to SiteSettings

def site_settings(request):
    """Make site settings available in all templates"""
    try:
        settings = SiteSettings.load()  # Changed from SiteSetting to SiteSettings
    except:
        # Fallback to default settings
        settings = SiteSettings()
    
    return {
        'site_settings': settings,
        'company_name': settings.company_name,
        'contact_phone': settings.contact_phone,
        'contact_email': settings.contact_email,
        'company_address': settings.company_address,
        'hero_title': settings.hero_title,
        'hero_description': settings.hero_description,
        'cta_title': settings.cta_title,
        'cta_description': settings.cta_description,
    }
