# services/models.py
from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from ckeditor.fields import RichTextField

class Service(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    detailed_content = models.TextField()
    # Short description for cards
    short_description = models.TextField(
        blank=True,
        help_text="Brief description shown on cards (max 150 characters)"
    )
    
    # Full description for detail page
    description = RichTextField(
        help_text="Full description shown on service detail page"
    )
    
    # Detailed content with features, benefits, etc.
    detailed_content = RichTextField(
        blank=True,
        help_text="Detailed content with features, benefits, process, etc."
    )
    
    # SEO fields
    meta_title = models.CharField(
        max_length=200,
        blank=True,
        help_text="SEO title (if empty, uses service title)"
    )
    
    meta_description = models.TextField(
        blank=True,
        max_length=160,
        help_text="SEO description (150-160 characters recommended)"
    )
    
    # Icon
    icon_image = models.ImageField(
        upload_to='service-icons/',
        blank=True,
        null=True,
        verbose_name="Service Icon",
        help_text="Upload an icon/image (100x100px PNG recommended)"
    )
    
    icon = models.CharField(
        max_length=100, 
        blank=True,
        default="fas fa-chart-line",
        help_text="Font Awesome icon (used if no image uploaded)"
    )
    
    # Featured image for detail page
    featured_image = models.ImageField(
        upload_to='service-featured/',
        blank=True,
        null=True,
        verbose_name="Featured Image",
        help_text="Large featured image for service detail page (recommended: 800x400px)"
    )
    
    # Additional fields for detail page
    key_features = models.TextField(
        blank=True,
        help_text="Key features (one per line)"
    )
    
    benefits = models.TextField(
        blank=True,
        help_text="Benefits (one per line)"
    )
    
    process = models.TextField(
        blank=True,
        help_text="Our process (one per line)"
    )
    
    # Pricing options (optional)
    has_pricing = models.BooleanField(
        default=False,
        help_text="Show pricing options for this service"
    )
    
    basic_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Basic Plan Price"
    )
    
    premium_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Premium Plan Price"
    )
    
    enterprise_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Enterprise Plan Price"
    )
    
    # Display settings
    display_order = models.IntegerField(default=0)
    is_featured = models.BooleanField(
        default=False,
        help_text="Feature this service on homepage"
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['display_order', 'title']
        verbose_name = "Service"
        verbose_name_plural = "Services"
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('service_detail', kwargs={'slug': self.slug})
    
    def get_meta_title(self):
        return self.meta_title or self.title
    
    def get_meta_description(self):
        if self.meta_description:
            return self.meta_description
        elif self.short_description:
            return self.short_description[:160]
        elif self.description:
            # Strip HTML tags for meta description
            import re
            clean_text = re.sub(r'<[^>]*>', '', str(self.description))
            return clean_text[:160]
        return ""
    
    def get_key_features_list(self):
        """Convert key features text to list"""
        if self.key_features:
            return [feature.strip() for feature in self.key_features.split('\n') if feature.strip()]
        return []
    
    def get_benefits_list(self):
        """Convert benefits text to list"""
        if self.benefits:
            return [benefit.strip() for benefit in self.benefits.split('\n') if benefit.strip()]
        return []
    
    def get_process_list(self):
        """Convert process text to list"""
        if self.process:
            return [step.strip() for step in self.process.split('\n') if step.strip()]
        return []