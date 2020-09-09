from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.models import User
from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from django.http import response
from django.contrib import auth
from api.models import (
    Workshop,
    Profile,
    Registration,
    Cart)
from api import views


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
