import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from catalog import forms
from catalog.models import Album

ALBUM_URL = reverse("catalog:album-list")


class PublicAlbumTest(TestCase):
    def test_login_required(self):
        response = self.client.get(ALBUM_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateAlbumTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="author",
            password="test_author_password",
        )
        self.client.force_login(self.user)

        number_of_albums = 13

        for album_id in range(number_of_albums):
            Album.objects.create(
                name=f"album_{album_id}",
                author=self.user,
                description="album description",
                release_date=datetime.date.today(),
            )

    def test_view_url_exists(self):
        response = self.client.get(ALBUM_URL)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(ALBUM_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/album_list.html")

    def test_view_have_search_form_context(self):
        response = self.client.get(ALBUM_URL)
        self.assertIn("search_form", response.context)
        self.assertIsInstance(
            response.context["search_form"], forms.AlbumSearchForm
        )

    def test_view_have_creation_form_context(self):
        response = self.client.get(reverse("catalog:album-create"))
        self.assertIsInstance(
            response.context["form"], forms.AlbumCreationForm
        )

    def test_view_have_update_form_context(self):
        response = self.client.get(
            reverse(
                "catalog:album-update", args=[Album.objects.first().pk]
            )
        )
        self.assertIsInstance(response.context["form"], forms.AlbumUpdateForm)

    def test_existing_pagination(self):
        response = self.client.get(ALBUM_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"] is True)
        self.assertEqual(len(response.context["album_list"]), 5)

    def test_pagination_paged(self):
        response = self.client.get(ALBUM_URL + "?page=3")
        self.assertEqual(len(response.context["album_list"]), 3)

    def test_correct_query_set(self):
        response = self.client.get(ALBUM_URL, {"name": "album_3"})
        self.assertContains(response, "album_3")
        self.assertNotContains(response, "album_4")

    def test_album_detail_view_exist(self):
        response = self.client.get(
            reverse("catalog:album-detail", args=[Album.objects.first().pk])
        )
        self.assertEqual(response.status_code, 200)

    def test_update_album_detail_view_exist(self):
        response = self.client.get(
            reverse("catalog:album-update", args=[Album.objects.first().pk])
        )
        self.assertEqual(response.status_code, 200)

    def test_delete_album_view_exist(self):
        response = self.client.get(
            reverse("catalog:album-delete", args=[Album.objects.first().pk])
        )
        self.assertEqual(response.status_code, 200)

    def test_assigning_in_album_detail_view_exist(self):
        response = self.client.get(
            reverse(
                "catalog:toggle-album-assign", args=[Album.objects.first().pk]
            )
        )
        self.assertEqual(response.status_code, 302)
