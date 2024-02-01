from django.contrib.auth.models import AbstractUser
from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=63, unique=True)

    def __str__(self):
        return self.name


class MusicAuthor(AbstractUser):
    creation_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.username}"


class Track(models.Model):
    name = models.CharField(max_length=100)
    duration = models.TimeField()
    author = models.ForeignKey(MusicAuthor, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)
    lyrics = models.TextField()

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return f"{self.name} with duration {self.duration}"


class Album(models.Model):
    name = models.CharField(max_length=255)
    tracks = models.ForeignKey(Track, on_delete=models.CASCADE)
    description = models.TextField()
    release_date = models.DateField()

    def __str__(self):
        return f"Album '{self.name}' was released on {self.release_date}"
