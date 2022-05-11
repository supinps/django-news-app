from django.contrib.auth.models import AbstractUser
from django.db import models

class PortalUser(AbstractUser):
    is_author = models.BooleanField('author status', default=False)
    is_editor = models.BooleanField('editor status', default=False)
    # add additional fields in here

    def __str__(self):
        return self.username
