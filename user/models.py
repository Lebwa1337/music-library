from django.contrib.auth.models import AbstractUser
from django.db import models


class MusicAuthor(AbstractUser):
    creation_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username
