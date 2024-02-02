from django.contrib.auth.models import AbstractUser
from django.db import models


class MusicAuthor(AbstractUser):
    band_members = models.TextField(blank=True, null=True)
    record_label = models.TextField(blank=True, null=True)
    creation_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username
