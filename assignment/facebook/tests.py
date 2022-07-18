from django.test import TestCase

from .models import User, Post


class UserModelTests(TestCase):


    def test_get_user_id(self):
        from django.test import Client
        client = Client()

        from django.urls import reverse
        response = client.get(reverse("userid", args=["7"]))

        assert response.status_code == 200


    def test_user(self):
        from django.test import Client
        client = Client()

        from django.urls import reverse
        response = client.get(reverse("user", args=["Lakshmi", "LakshmiPost", "LakshmiPostDescription"]))

        assert response.status_code == 200


    def test_delete_user(self):
        from django.test import Client
        client = Client()

        from django.urls import reverse
        response = client.get(reverse("userid", args=["7"]))

        assert response.status_code == 200
