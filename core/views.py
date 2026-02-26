"""
Core app views for StartMarket website.
Handles all page rendering and contact form submission.
"""

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm


def home(request):
    """Render the homepage with hero, services, process, and CTA sections."""
    context = {
        'meta_title': 'StartMarket — Building MVPs for Startups',
        'meta_description': 'StartMarket helps startups launch fast by building MVPs, custom websites, and scalable software products. Book a free consultation today.',
        'og_title': 'StartMarket — Building MVPs for Startups',
        'og_description': 'We build MVPs that launch startups faster. MVP Development, Custom Websites, SaaS, Consulting.',
    }
    return render(request, 'home.html', context)


def services(request):
    """Render the services page with detailed service offerings."""
    services_data = [
        {
            'icon': '⚡',
            'title': 'MVP Development',
            'tagline': 'From idea to live product in weeks.',
            'description': 'We build your Minimum Viable Product with production-ready code, so you can validate your idea, attract investors, and start growing—fast.',
            'deliverables': [
                'Full-stack web or mobile app',
                'Database design & API',
                'Admin panel',
                'Deployment on cloud',
                'Source code handoff',
            ],
            'timeline': '4–8 weeks',
            'price': 'Starting at ₹60,000',
            'slug': 'mvp-development',
        },
        {
            'icon': '🌐',
            'title': 'Custom Websites',
            'tagline': 'Your digital presence, perfected.',
            'description': 'High-performance, conversion-optimised websites that tell your brand story and turn visitors into customers. No templates—fully custom.',
            'deliverables': [
                'Responsive design',
                'SEO-optimised pages',
                'CMS integration',
                'Contact & lead forms',
                'Analytics setup',
            ],
            'timeline': '1–3 weeks',
            'price': 'Starting at ₹20,000',
            'slug': 'custom-websites',
        },
        {
            'icon': '🚀',
            'title': 'SaaS Development',
            'tagline': 'Scalable software, built right.',
            'description': 'End-to-end SaaS product development—auth, billing, dashboards, multi-tenancy, and everything in between. Built for scale from day one.',
            'deliverables': [
                'User authentication & roles',
                'Subscription & billing (Stripe/Razorpay)',
                'Multi-tenant architecture',
                'REST APIs',
                'Cloud deployment & CI/CD',
            ],
            'timeline': '8–16 weeks',
            'price': 'Starting at ₹1,20,000',
            'slug': 'saas-development',
        },
        {
            'icon': '🧠',
            'title': 'Startup Tech Consulting',
            'tagline': 'Strategy before a single line of code.',
            'description': 'Get expert guidance on your tech stack, architecture decisions, and product roadmap. Avoid costly mistakes before you build.',
            'deliverables': [
                'Tech stack recommendation',
                'Architecture blueprint',
                'Product roadmap',
                'Team structure advice',
                'Investor-ready tech deck',
            ],
            'timeline': '1–2 weeks',
            'price': 'Starting at ₹10,000',
            'slug': 'consulting',
        },
    ]
    context = {
        'meta_title': 'Services — StartMarket',
        'meta_description': 'MVP Development, Custom Websites, SaaS Development, and Startup Tech Consulting by StartMarket.',
        'services': services_data,
    }
    return render(request, 'services.html', context)


def about(request):
    """Render the about page with founder story and mission."""
    context = {
        'meta_title': 'About — StartMarket',
        'meta_description': 'StartMarket is a founder-led tech studio helping startups launch faster with MVPs and custom software.',
    }
    return render(request, 'about.html', context)


def portfolio(request):
    """Render the portfolio page with project showcase."""
    projects = [
        {
            'title': 'FinTrack',
            'category': 'SaaS · FinTech',
            'description': 'Personal finance tracker with AI-powered insights, budget alerts, and multi-bank sync.',
            'tags': ['Django', 'React', 'PostgreSQL', 'OpenAI'],
            'year': '2024',
        },
        {
            'title': 'LaunchPad',
            'category': 'MVP · EdTech',
            'description': 'Online learning platform with live sessions, course builder, and payment integration.',
            'tags': ['Django', 'WebSockets', 'Stripe', 'AWS'],
            'year': '2024',
        },
        {
            'title': 'GreenCart',
            'category': 'E-Commerce · Sustainability',
            'description': 'Sustainable products marketplace with vendor management and carbon footprint tracker.',
            'tags': ['Django', 'Razorpay', 'Redis', 'Docker'],
            'year': '2023',
        },
        {
            'title': 'MediBook',
            'category': 'MVP · HealthTech',
            'description': 'Doctor appointment booking platform with telemedicine features and EHR integration.',
            'tags': ['Django', 'Twilio', 'PostgreSQL', 'Celery'],
            'year': '2023',
        },
        {
            'title': 'PropertyPulse',
            'category': 'SaaS · PropTech',
            'description': 'Real estate listing platform with virtual tours, lead management, and analytics.',
            'tags': ['Django', 'Maps API', 'S3', 'Elasticsearch'],
            'year': '2023',
        },
        {
            'title': 'LocalBite',
            'category': 'MVP · FoodTech',
            'description': 'Hyperlocal food delivery connecting home chefs with customers near them.',
            'tags': ['Django', 'FCM', 'Razorpay', 'Flutter'],
            'year': '2022',
        },
    ]
    context = {
        'meta_title': 'Portfolio — StartMarket',
        'meta_description': 'Explore MVPs and digital products built by StartMarket for startups across industries.',
        'projects': projects,
    }
    return render(request, 'portfolio.html', context)


def contact(request):
    """Handle the contact page and form submission."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()
            # Send notification email (console backend in dev)
            try:
                send_mail(
                    subject=f"New Enquiry from {contact_message.name} — StartMarket",
                    message=f"""
New contact form submission:

Name: {contact_message.name}
Email: {contact_message.email}
Company: {contact_message.company or '—'}
Service: {contact_message.get_service_display()}

Message:
{contact_message.message}
                    """.strip(),
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_EMAIL],
                    fail_silently=True,
                )
            except Exception:
                pass
            messages.success(request, 'success')
            return redirect('core:contact')
        else:
            messages.error(request, 'error')
    else:
        form = ContactForm()

    context = {
        'meta_title': 'Contact — StartMarket',
        'meta_description': 'Book a free consultation with StartMarket. We help startups launch fast.',
        'form': form,
    }
    return render(request, 'contact.html', context)
