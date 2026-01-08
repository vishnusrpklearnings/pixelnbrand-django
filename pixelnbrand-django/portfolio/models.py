# portfolio/models.py
from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from ckeditor.fields import RichTextField

class PortfolioItem(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    detailed_description = RichTextField(blank=True)  # Add this for detailed page
    category = models.CharField(max_length=50, default='General')
    image = models.ImageField(upload_to='portfolio/')
    
    # Additional fields for detailed page
    client_name = models.CharField(max_length=100, blank=True)
    project_date = models.DateField(null=True, blank=True)
    project_url = models.URLField(blank=True, verbose_name="Project URL/Live Demo")
    technologies = models.CharField(max_length=200, blank=True, help_text="Comma-separated list of technologies used")
    
    # Multiple images for detailed page
    image_2 = models.ImageField(upload_to='portfolio/', blank=True, null=True)
    image_3 = models.ImageField(upload_to='portfolio/', blank=True, null=True)
    
    is_featured = models.BooleanField(default=False)
    display_order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['display_order']
        verbose_name = "Portfolio Item"
        verbose_name_plural = "Portfolio Items"
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('portfolio_detail', kwargs={'slug': self.slug})
    
    def get_technologies_list(self):
        """Convert comma-separated technologies to list"""
        if self.technologies:
            return [tech.strip() for tech in self.technologies.split(',')]
        return []