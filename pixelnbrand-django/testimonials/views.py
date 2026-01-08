from django.shortcuts import render
from .models import Testimonial

def testimonial_list(request):
    testimonials = Testimonial.objects.filter(is_active=True).order_by('display_order')
    return render(request, 'testimonials/list.html', {'testimonials': testimonials})

def index(request):
    return render(request, 'testimonials/index.html')
