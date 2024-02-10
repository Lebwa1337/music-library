from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from catalog import forms
from catalog.models import Genre

GENRE_URL = reverse("catalog:genre-list")


class PublicGenreTest(TestCase):
    def test_login_required(self):
        response = self.client.get(GENRE_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateGenreTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="author",
            password="test_author_password",
        )
        self.client.force_login(self.user)

        number_of_genre = 13

        for genre_id in range(number_of_genre):
            Genre.objects.create(
                name=f"genre-{genre_id}"
            )

    def test_view_url_exists(self):
        response = self.client.get(GENRE_URL)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(GENRE_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/genre_list.html")

    def test_view_have_search_form_context(self):
        response = self.client.get(GENRE_URL)
        self.assertIn("search_form", response.context)
        self.assertIsInstance(
            response.context["search_form"],
            forms.GenreSearchForm
        )

    def test_view_have_creation_form_context(self):
        response = self.client.get(reverse("catalog:genre-create"))
        self.assertIsInstance(
            response.context["form"],
            forms.GenreForm
        )

    def test_view_have_update_form_context(self):
        response = self.client.get(
            reverse("catalog:genre-update", args=[Genre.objects.first().pk])
        )
        self.assertIsInstance(
            response.context["form"],
            forms.GenreForm
        )

    def test_existing_pagination(self):
        response = self.client.get(GENRE_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"] is True)
        self.assertEqual(len(response.context["genre_list"]), 5)

    def test_pagination_paged(self):
        response = self.client.get(GENRE_URL + "?page=3")
        self.assertEqual(len(response.context["genre_list"]), 3)

    def test_correct_query_set(self):
        response = self.client.get(GENRE_URL, {"name": "genre-3"})
        self.assertContains(response, "genre-3")
        self.assertNotContains(response, "genre-4")

    def test_update_genre_view_exist(self):
        response = self.client.get(
            reverse("catalog:genre-update", args=[Genre.objects.first().pk])
        )
        self.assertEqual(response.status_code, 200)

    def test_delete_genre_view_exist(self):
        response = self.client.get(
            reverse("catalog:genre-delete", args=[Genre.objects.first().pk])
        )
        self.assertEqual(response.status_code, 200)
