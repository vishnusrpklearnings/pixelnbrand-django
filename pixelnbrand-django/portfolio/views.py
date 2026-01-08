# portfolio/views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import PortfolioItem

def portfolio_list(request):
    """Portfolio list view with filtering"""
    portfolio_items = PortfolioItem.objects.all().order_by('display_order')
    
    # Get unique categories for filter
    categories = PortfolioItem.objects.values_list('category', flat=True).distinct()
    
    context = {
        'portfolio_items': portfolio_items,
        'categories': categories,
    }
    return render(request, 'portfolio/list.html', context)

def portfolio_detail(request, slug):
    """Portfolio detail view"""
    portfolio_item = get_object_or_404(PortfolioItem, slug=slug)
    
    # Get related portfolio items (same category, excluding current)
    related_items = PortfolioItem.objects.filter(
        category=portfolio_item.category
    ).exclude(
        id=portfolio_item.id
    ).order_by('display_order')[:3]
    
    context = {
        'portfolio': portfolio_item,
        'related_items': related_items,
    }
    return render(request, 'portfolio/detail.html', context)