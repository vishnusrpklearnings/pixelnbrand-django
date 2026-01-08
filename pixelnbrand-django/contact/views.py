from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import ContactMessage
from agency.models import SiteSettings
import socket

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Save to database
        contact_msg = ContactMessage(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message,
            ip_address=request.META.get('REMOTE_ADDR'),
            user_agent=request.META.get('HTTP_USER_AGENT', '')
        )
        contact_msg.save()
        
        # Send email notification
        try:
            contact_email = SiteSetting.objects.filter(key='contact_email').first()
            if contact_email:
                send_mail(
                    f'New Contact Form Submission: {subject}',
                    f'Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}',
                    'noreply@pixelnbrand.com',
                    [contact_email.value],
                    fail_silently=False,
                )
        except Exception as e:
            print(f"Email error: {e}")
        
        messages.success(request, 'Thank you for your message! We will get back to you soon.')
        return redirect('contact')
    
    return render(request, 'contact/index.html')