from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from agency.views import home, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('services/', include('services.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('testimonials/', include('testimonials.urls')),
    path('contact/', include('contact.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Custom admin site header
admin.site.site_header = "Pixel & Brand Admin"
admin.site.site_title = "Pixel & Brand Admin Portal"
admin.site.index_title = "Welcome to Pixel & Brand Admin"