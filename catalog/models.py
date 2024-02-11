from django.db import models

from user.models import MusicAuthor


class Genre(models.Model):
    name = models.CharField(max_length=63, unique=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(
        MusicAuthor,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="albums",
    )
    description = models.TextField()
    release_date = models.DateField()

    def __str__(self):
        return f"Album '{self.name}' was released on {self.release_date}"


class Track(models.Model):
    name = models.CharField(max_length=100)
    duration = models.DurationField()
    author = models.ForeignKey(
        MusicAuthor, on_delete=models.CASCADE, related_name="tracks"
    )
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        related_name="tracks"
    )
    genre = models.ManyToManyField(Genre, related_name="tracks")
    lyrics = models.TextField()

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return f"{self.name} with duration {self.duration}"
