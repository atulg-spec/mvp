"""
Core app models for StartMarket.
"""

from django.db import models


class ContactMessage(models.Model):
    """Stores contact form submissions from the StartMarket website."""
    name = models.CharField(max_length=200)
    email = models.EmailField()
    company = models.CharField(max_length=200, blank=True)
    service = models.CharField(
        max_length=100,
        choices=[
            ('mvp', 'MVP Development'),
            ('website', 'Custom Website'),
            ('saas', 'SaaS Development'),
            ('consulting', 'Startup Tech Consulting'),
            ('other', 'Other'),
        ],
        default='other'
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'

    def __str__(self):
        return f"{self.name} — {self.email} ({self.created_at.strftime('%Y-%m-%d')})"
