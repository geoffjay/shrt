import random
import string

from django.db import models

class Url(models.Model):
    name = models.CharField(max_length=255)
    shortened = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        # Generate a random 4 character tag on save
        letters = string.ascii_letters + string.digits
        self.shortened = ''.join(random.choice(letters) for i in range(4))
        super().save(*args, **kwargs)

    def __str__(self):
        """String for representing the Model object."""
        return self.name
