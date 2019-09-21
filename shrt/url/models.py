import random
import string
import time

from django.db import models

def GenerateTag():
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
    original = models.CharField(max_length=255)
    tag = models.CharField(max_length=4, default=GenerateTag)

    def __str__(self):
        """String for representing the URL model."""
        return '%s -> %s' % (self.tag, self.original)
