import random
import string
import datetime

from django.db import models

class Url(models.Model):
    """Url model.

    Used to persist shortened URL entries.

    Attributes:
        original (str): The full URL to provide when requested by tag.
        shortened (str): The shortened URL containing the host and tag.
        tag (str): A tag representing the shortened URL.
    """
    original = models.CharField(max_length=255)
    shortened = models.CharField(max_length=255)
    tag = models.CharField(max_length=4)

    def save(self, *args, **kwargs):
        """Generate a random 4 character tag on save."""
        letters = string.ascii_letters + string.digits
        random.seed(datetime.time.microsecond)
        self.shortened = ''.join(random.choice(letters) for i in range(4))
        # should check for existing tag and keep trying if one is found
        super().save(*args, **kwargs)

    def __str__(self):
        """String for representing the Model object."""
        return self.original
