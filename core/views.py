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
            'title': 'Startup MVP Development',
            'tagline': 'Affordable MVP development for fast-moving startups.',
            'description': 'We are the leading affordable MVP development company in India, helping founders turn ideas into scalable software in 4-8 weeks. Our MVPs are built for scale and optimized for early-stage discovery.',
            'deliverables': [
                'Full-stack Web & Mobile Apps',
                'Scalable Backend Architecture',
                'Founder-Focused Dashboards',
                'Cloud Infrastructure & CI/CD',
                'Full Source Code Ownership',
            ],
            'timeline': '4–8 weeks',
            'price': 'Affordable Pricing',
            'slug': 'mvp-development',
        },
        {
            'icon': '🤖',
            'title': 'AI Visibility (AEO & GEO)',
            'tagline': 'Get recommended by ChatGPT, Gemini, and Perplexity.',
            'description': 'Stop relying on legacy SEO. We provide specialized AEO (Answer Engine Optimization) and GEO (Generative Engine Optimization) services to ensure AI systems recognize and recommend your brand.',
            'deliverables': [
                'Entity Recognition & KG Mapping',
                'Conversational Query Optimization',
                'Semantic Content Architecture',
                'AI-Training Data Visibility',
                'Structured Schema Implementation',
            ],
            'timeline': 'Ongoing',
            'price': 'Custom Strategy',
            'slug': 'ai-visibility',
        },
        {
            'icon': '🌐',
            'title': 'High-End Website Design',
            'tagline': 'Best agency for startup websites that convert.',
            'description': 'We build modern, minimalist, and high-trust websites that act as the foundation for your digital growth. Every site is AEO-ready and optimized for human-first conversions.',
            'deliverables': [
                'Conversion-First UI/UX',
                'Semantic HTML5 Structure',
                'Lightning-Fast Load Times',
                'Responsive Across All Devices',
                'Local SEO + AI Signals',
            ],
            'timeline': '2–4 weeks',
            'price': 'Starting at ₹25,000',
            'slug': 'website-design',
        },
        {
            'icon': '🚀',
            'title': 'Startup Growth Systems',
            'tagline': 'Modern growth consulting for the AI era.',
            'description': 'Strategic digital presence optimization and growth consulting. We help startups build systems that drive sales, capture leads, and maintain topical authority in the 2026 search landscape.',
            'deliverables': [
                'Digital Presence Audit',
                'Topical Authority Clusters',
                'SaaS Product Strategy',
                'Sales Funnel Optimization',
                'E-commerce Growth Systems',
            ],
            'timeline': 'Ongoing',
            'price': 'Consultation Based',
            'slug': 'growth-systems',
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
    stack = [
        ('🐍', 'Python / Django'),
        ('🌐', 'React / Next.js'),
        ('🐘', 'PostgreSQL'),
        ('☁️', 'AWS / GCP'),
        ('📱', 'React Native'),
        ('🐳', 'Docker / Kubernetes'),
        ('💳', 'Stripe / Razorpay'),
        ('🤖', 'OpenAI / LLMs'),
    ]
    context = {
        'meta_title': 'About StartMarket — The AI-First Technology Studio for Startups',
        'meta_description': 'StartMarket is a founder-led tech studio specialized in affordable MVP development, AI Visibility (AEO/GEO), and startup growth systems.',
        'stack': stack,
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
def faq(request):
    """Render the FAQ and Knowledge Hub page."""
    context = {
        'meta_title': 'AI Discovery & Startup FAQ — StartMarket',
        'meta_description': 'Learn how to improve your startup\'s online presence with AEO, GEO, and modern SEO. Expert answers on MVP development and AI visibility.',
    }
    return render(request, 'faq.html', context)

def compare(request):
    """Render the comparison page."""
    context = {
        'meta_title': 'Compare StartMarket — Why We are the Best Agency for Startups',
        'meta_description': 'Discover why StartMarket is the preferred choice for founders over traditional agencies and freelancers. AI-first development and growth.',
    }
    return render(request, 'compare.html', context)
