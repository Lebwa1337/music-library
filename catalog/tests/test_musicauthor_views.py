from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from user import forms
from user.models import MusicAuthor

MUSICAUTHOR_URL = reverse("user:author-list")


class PublicMusicAuthorTest(TestCase):
    def test_login_required(self):
        response = self.client.get(MUSICAUTHOR_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateMusicAuthorTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="author",
            password="test_author_password",
        )
        self.client.force_login(self.user)

        number_of_author = 12

        for author_id in range(number_of_author):
            MusicAuthor.objects.create_user(
                username=f"Author {author_id}",
                password=f"password12{author_id}",
            )

    def test_view_url_exists(self):
        response = self.client.get(MUSICAUTHOR_URL)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(MUSICAUTHOR_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/music_author_list.html")

    def test_view_have_search_form_context(self):
        response = self.client.get(MUSICAUTHOR_URL)
        self.assertIn("search_form", response.context)
        self.assertIsInstance(
            response.context["search_form"], forms.MusicAuthorSearchForm
        )

    def test_view_have_creation_form_context(self):
        response = self.client.get(reverse("user:author-create"))
        self.assertIsInstance(
            response.context["form"], forms.MusicAuthorCreationForm
        )

    def test_view_have_update_form_context(self):
        response = self.client.get(
            reverse(
                "user:author-update", args=[MusicAuthor.objects.first().pk]
            )
        )
        self.assertIsInstance(
            response.context["form"], forms.MusicAuthorUpdateForm
        )

    def test_existing_pagination(self):
        response = self.client.get(MUSICAUTHOR_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"] is True)
        self.assertEqual(len(response.context["musicauthor_list"]), 5)

    def test_pagination_paged(self):
        response = self.client.get(MUSICAUTHOR_URL + "?page=3")
        self.assertEqual(len(response.context["musicauthor_list"]), 3)

    def test_correct_query_set(self):
        response = self.client.get(MUSICAUTHOR_URL, {"username": "Author 3"})
        self.assertContains(response, "Author 3")
        self.assertNotContains(response, "Author 4")

    def test_music_author_detail_view_exist(self):
        response = self.client.get(
            reverse(
                "user:author-detail",
                args=[MusicAuthor.objects.first().pk]
            )
        )
        self.assertEqual(response.status_code, 200)

    def test_update_music_author_detail_view_exist(self):
        response = self.client.get(
            reverse(
                "user:author-update",
                args=[MusicAuthor.objects.first().pk]
            )
        )
        self.assertEqual(response.status_code, 200)

    def test_delete_music_author_view_exist(self):
        response = self.client.get(
            reverse(
                "user:author-delete",
                args=[MusicAuthor.objects.first().pk]
            )
        )
        self.assertEqual(response.status_code, 200)
