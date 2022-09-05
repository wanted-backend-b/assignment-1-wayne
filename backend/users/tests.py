import json
import jwt
import os

from django.test import TestCase, Client

from postings.models import FreeBoardPosting, FreeComment, FreeView
from .models import User


class TestSignUpView(TestCase):
    def setUp(self):
        self.client = Client()
