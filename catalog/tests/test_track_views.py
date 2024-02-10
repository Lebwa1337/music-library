import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from catalog import forms
from catalog.models import Track, Album, Genre

TRACK_URL = reverse("catalog:track-list")


class PublicTrackTest(TestCase):
    def test_login_required(self):
        response = self.client.get(TRACK_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateTrackTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="author",
            password="test_author_password",
        )
        self.client.force_login(self.user)

        number_of_tracks = 13

        for track_id in range(number_of_tracks):
            track = Track.objects.create(
                name=f"Track {track_id}",
                duration=datetime.timedelta(minutes=5),
                author=self.user,
                album=Album.objects.create(
                    name=f"Album{track_id}",
                    author=self.user,
                    description=f"Description{track_id}",
                    release_date=datetime.date.today()
                ),
                lyrics=f"Lyrics{track_id}"
            )
            track.genre.set([Genre.objects.create(
                name=f"Genre{track_id}"
            )]
            )

    def test_view_url_exists(self):
        response = self.client.get(TRACK_URL)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(TRACK_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/track_list.html")

    def test_view_have_search_form_context(self):
        response = self.client.get(TRACK_URL)
        self.assertIn("search_form", response.context)
        self.assertIsInstance(
            response.context["search_form"],
            forms.TrackSearchForm
        )

    def test_view_have_creation_form_context(self):
        response = self.client.get(reverse("catalog:track-create"))
        self.assertIsInstance(
            response.context["form"],
            forms.TrackForm
        )

    def test_view_have_update_form_context(self):
        response = self.client.get(
            reverse("catalog:track-update", args=[Track.objects.first().pk])
        )
        self.assertIsInstance(
            response.context["form"],
            forms.TrackForm
        )

    def test_existing_pagination(self):
        response = self.client.get(TRACK_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"] is True)
        self.assertEqual(len(response.context["track_list"]), 5)

    def test_pagination_paged(self):
        response = self.client.get(TRACK_URL + "?page=3")
        self.assertEqual(len(response.context["track_list"]), 3)

    def test_correct_query_set(self):
        response = self.client.get(TRACK_URL, {"name": "Track 3"})
        self.assertContains(response, "Track 3")
        self.assertNotContains(response, "Track 4")

    def test_track_detail_view_exist(self):
        response = self.client.get(
            reverse("catalog:track-detail", args=[Track.objects.first().pk])
        )
        self.assertEqual(response.status_code, 200)

    def test_update_track_detail_view_exist(self):
        response = self.client.get(
            reverse("catalog:track-update", args=[Track.objects.first().pk])
        )
        self.assertEqual(response.status_code, 200)

    def test_delete_track_view_exist(self):
        response = self.client.get(
            reverse("catalog:track-delete", args=[Track.objects.first().pk])
        )
        self.assertEqual(response.status_code, 200)
