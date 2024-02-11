import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from catalog.models import Album, Track, Genre
from user.models import MusicAuthor


class SearchFormsTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="user_login",
            password="123123password",
        )
        self.album1 = Album.objects.create(
            name="Album1",
            author=self.user,
            description="album description",
            release_date=datetime.date.today(),
        )
        self.album2 = Album.objects.create(
            name="Album2",
            author=self.user,
            description="album description2",
            release_date=datetime.date.today(),
        )
        self.genre1 = Genre.objects.create(name="Genre1")
        self.genre2 = Genre.objects.create(name="Genre2")
        self.track1 = Track.objects.create(
            name="Track1",
            album=self.album1,
            author=self.user,
            duration=datetime.timedelta(minutes=5),
            lyrics="album lyrics1",
        )
        self.track1.genre.set([self.genre1])

        self.track2 = Track.objects.create(
            name="Track2",
            album=self.album2,
            author=self.user,
            duration=datetime.timedelta(minutes=6),
            lyrics="album lyrics2",
        )
        self.track2.genre.set([self.genre2])

        self.client.force_login(self.user)

    def test_music_author_query_set_changed_after_form(self):
        filtered_queryset = MusicAuthor.objects.filter(username="user_login")
        response = self.client.get(
            reverse("user:author-list"), {"username": "user_login"}
        )
        query_set_after_search = response.context["musicauthor_list"]
        self.assertEqual(list(query_set_after_search), list(filtered_queryset))

    def test_album_query_set_changed_after_form(self):
        filtered_queryset = Album.objects.filter(name="Album1")
        response = self.client.get(
            reverse("catalog:album-list"), {"name": "Album1"}
        )
        query_set_after_search = response.context["album_list"]
        self.assertEqual(list(query_set_after_search), list(filtered_queryset))

    def test_genre_query_set_changed_after_form(self):
        filtered_queryset = Genre.objects.filter(name="Genre1")
        response = self.client.get(
            reverse("catalog:genre-list"), {"name": "Genre1"}
        )
        query_set_after_search = response.context["genre_list"]
        self.assertEqual(list(query_set_after_search), list(filtered_queryset))

    def test_track_query_set_changed_after_form(self):
        filtered_queryset = Track.objects.filter(name="Track1")
        response = self.client.get(
            reverse("catalog:track-list"), {"name": "Track1"}
        )
        query_set_after_search = response.context["track_list"]
        self.assertEqual(list(query_set_after_search), list(filtered_queryset))
