# agency/models.py
from django.db import models

class SiteSettings(models.Model):
    """User-friendly site settings with proper field names"""
    
    # Company Information
    company_name = models.CharField(
        max_length=200,
        default="Pixel & Brand",
        verbose_name="Company Name",
        help_text="The name of your company that appears throughout the site"
    )
    
    logo = models.ImageField(
        upload_to='logos/',
        blank=True,
        null=True,
        verbose_name="Company Logo",
        help_text="Upload your company logo. Recommended size: 200x60px"
    )
    
    logo_alt_text = models.CharField(
        max_length=200,
        blank=True,
        default="Pixel & Brand Logo",
        verbose_name="Logo Alt Text",
        help_text="Description of the logo for accessibility (shown if logo doesn't load)"
    )
    
    show_logo_only = models.BooleanField(
        default=False,
        verbose_name="Show Only Logo",
        help_text="Check this to show only the logo without company name text"
    )
    
    tagline = models.CharField(
        max_length=200,
        blank=True,
        default="Digital Marketing Agency in Kerala",
        verbose_name="Company Tagline",
        help_text="Short tagline that appears in footer and page titles"
    )
    
    # Hero Section
    hero_title = models.CharField(
        max_length=200,
        blank=True,
        default="Transform Your Digital Presence",
        verbose_name="Hero Title",
        help_text="Main title on the homepage hero section"
    )
    
    hero_description = models.TextField(
        blank=True,
        default="We help businesses grow their online presence with cutting-edge digital marketing strategies tailored to your goals.",
        verbose_name="Hero Description",
        help_text="Description under the hero title"
    )
    
    hero_button_text = models.CharField(
        max_length=50,
        blank=True,
        default="Get Started Today",
        verbose_name="Hero Button Text",
        help_text="Text for the hero section button"
    )
    
    hero_image = models.ImageField(
        upload_to='homepage/',
        blank=True,
        null=True,
        verbose_name="Hero Image",
        help_text="Image for the hero section (recommended: 800x600px)"
    )
    
    # Services Section
    services_title = models.CharField(
        max_length=200,
        blank=True,
        default="Our Services",
        verbose_name="Services Title",
        help_text="Title for the services section"
    )
    
    services_description = models.TextField(
        blank=True,
        default="End-to-end digital solutions to grow your brand, connect with your audience, and drive real results.",
        verbose_name="Services Description",
        help_text="Description for the services section"
    )
    
    # Testimonials Section
    testimonials_title = models.CharField(
        max_length=200,
        blank=True,
        default="What Our Clients Say",
        verbose_name="Testimonials Title",
        help_text="Title for the testimonials section"
    )
    
    testimonials_description = models.TextField(
        blank=True,
        default="Hear from businesses that have transformed their digital presence with our solutions.",
        verbose_name="Testimonials Description",
        help_text="Description for the testimonials section"
    )
    
    # Portfolio Section
    portfolio_title = models.CharField(
        max_length=200,
        blank=True,
        default="Our Recent Work",
        verbose_name="Portfolio Title",
        help_text="Title for the portfolio section"
    )
    
    portfolio_description = models.TextField(
        blank=True,
        default="Explore our portfolio of successful digital marketing projects and brand transformations.",
        verbose_name="Portfolio Description",
        help_text="Description for the portfolio section"
    )
    
    # CTA Section
    cta_title = models.CharField(
        max_length=200,
        blank=True,
        default="Ready to Grow Your Business?",
        verbose_name="CTA Title",
        help_text="Title for the call-to-action section"
    )
    
    cta_description = models.TextField(
        blank=True,
        default="Let's work together to create amazing digital experiences that drive results.",
        verbose_name="CTA Description",
        help_text="Description for the call-to-action section"
    )
    
    cta_button_text = models.CharField(
        max_length=50,
        blank=True,
        default="Get In Touch",
        verbose_name="CTA Button Text",
        help_text="Text for the call-to-action button"
    )
    
    # Contact Information
    contact_phone = models.CharField(
        max_length=20,
        blank=True,
        default="+91 80864-88003",
        verbose_name="Phone Number",
        help_text="Contact phone number displayed in header/footer"
    )
    
    contact_email = models.EmailField(
        blank=True,
        default="info@craftrix.com",
        verbose_name="Email Address",
        help_text="Contact email displayed in header/footer"
    )
    
    company_address = models.TextField(
        blank=True,
        default="Craftrix Consultancy Services Pvt Ltd, Udarasiromani Rd, Thiruvananthapuram, Kerala 695010",
        verbose_name="Company Address",
        help_text="Full company address for contact section"
    )
    
    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"
    
    def __str__(self):
        return "Website Configuration"
    
    def save(self, *args, **kwargs):
        # Ensure only one instance exists
        self.pk = 1
        super().save(*args, **kwargs)
    
    @classmethod
    def load(cls):
        """Get or create the single settings instance"""
        obj, created = cls.objects.get_or_create(pk=1)
        return obj