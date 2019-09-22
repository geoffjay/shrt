import random
import string
import time

from django.db import models
from django.conf import settings

def site():
    if settings.SITE_PORT is None:
        return '%s://%s' % (settings.SITE_PROTOCOL, settings.SITE_DOMAIN)
    else:
        return '%s://%s:%s' % (settings.SITE_PROTOCOL, settings.SITE_DOMAIN, settings.SITE_PORT)

def generate_tag():
    """Generate a random 4 character tag on save."""
    letters = string.ascii_letters + string.digits
    random.seed(time.time())
    return ''.join(random.choice(letters) for i in range(4))


class Url(models.Model):
    """Url model.

    Used to persist shortened URL entries.

    Attributes:
        original (str): The full URL to provide when requested by tag.
        tag (str): A tag representing the shortened URL.
    """

    # according to the internet 2000 characters is reasonable to assume
    original = models.CharField(max_length=2000)
    tag = models.CharField(max_length=4, default=generate_tag)
    shortened = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        self.shortened = '%s/%s' % (site(), self.tag)
        super().save(*args, **kwargs)

    def __str__(self):
        """String for representing the URL model."""
        return '%s -> %s' % (self.tag, self.original)
