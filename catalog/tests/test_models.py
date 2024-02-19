import datetime

from django.test import TestCase
from django.urls import reverse

from catalog.models import Genre, Album, Track
from user.models import MusicAuthor


class TestModels(TestCase):
    def setUp(self) -> None:
        self.genre = Genre.objects.create(
            name="test_genre_name",
        )
        self.author = MusicAuthor.objects.create(
            username="test_author",
        )
        self.album = Album.objects.create(
            name="test_album_name",
            author=self.author,
            description="test album description",
            release_date=datetime.date.today(),
        )
        self.track = Track.objects.create(
            name="test_track_name",
            album=self.album,
            author=self.author,
            duration=datetime.timedelta(minutes=5),
            lyrics="dummy_lyrics",
        )
        self.track.genre.set([self.genre])

    def test_string_representation(self):
        self.assertEqual(
            str(self.genre),
            self.genre.name,
        )
        self.assertEqual(
            str(self.album),
            f"Album '{self.album.name}' "
            f"was released on {self.album.release_date}",
        )
        self.assertEqual(
            str(self.track),
            f"{self.track.name} with duration {self.track.duration}"
        )

    def test_musicauthor_get_absolute_url(self):
        expected_url = reverse(
            "user:author-detail", kwargs={"pk": self.author.pk}
        )
        actual_url = self.author.get_absolute_url()
        self.assertEqual(expected_url, actual_url)
