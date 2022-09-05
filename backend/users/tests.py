import json

import bcrypt
import jwt
import os

from django.test import TestCase, Client

from .models import User


class SignUpTest(TestCase):
    def setUp(self):
        hashed_password = bcrypt.hashpw(
            'testtest'.encode('utf-8'), bcrypt.gensalt()
        ).decode('utf-8')

        User.objects.create(
            name='unit_test',
            email='unit_test@test.com',
            psword=hashed_password,
            gender='m',
            age='20',
            phone_number='010-1234-5678',
            level='1'
        )

    def tearDown(self):
        User.objects.all().delete()
        print("signup end")

    def test_signup_success(self):
        '''
        회원가입 테스트
        '''
        client = Client()

        test_user = {
            'name': 'unit_test1',
            'email': 'unit_test1@test.com',
            'psword': 'testtest',
            'gender': 'm',
            'age': '20',
            'phone_number': '010-1234-5678',
            'level': '1'
        }
        response = self.client.post(
            "/users/signup", json.dumps(test_user), content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {"message": "회원가입 완료"})


class LogInTest(TestCase):
    def setUp(self):
        hashed_password = bcrypt.hashpw(
            'testtest'.encode('utf-8'), bcrypt.gensalt()
        ).decode('utf-8')

        User.objects.create(
            name='unit_test',
            email='unit_test@test.com',
            psword=hashed_password,
            gender='m',
            age='20',
            phone_number='010-1234-5678',
            level='1'
        )

    def tearDown(self):
        User.objects.all().delete()
        print("login end")

    def test_login(self):
        client = Client()

        user = {
            'email': 'unit_test@test.com',
            'psword': 'testtest'
        }

        response = client.post(
            '/users/login',
            json.dumps(user),
            content_type='application/json'
        )

        token = jwt.encode(
            {"user_id": 1},
            os.environ.get("SECRET"),
            os.environ.get("ALGORITHM"),
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"token": token})


class WithdrawalTest(TestCase):
    def setUp(self):
        hashed_password = bcrypt.hashpw(
            'testtest'.encode('utf-8'), bcrypt.gensalt()
        ).decode('utf-8')

        User.objects.create(
            id=1,
            name='unit_test',
            email='unit_test@test.com',
            psword=hashed_password,
            gender='m',
            age='20',
            phone_number='010-1234-5678',
            level='1'
        )

        self.token = jwt.encode(
            {"user_id": 1},
            os.environ.get("SECRET"),
            os.environ.get("ALGORITHM"),
        )

    def tearDown(self):
        User.objects.all().delete()
        print("Withdrawal end")

    def test_WithdrawalV(self):
        client = Client()

        headers = {
            'HTTP_Authorization': self.token
        }

        user = {
            'email': 'unit_test@test.com',
            'psword': 'testtest'
        }

        response = client.post(
            '/users/withdrawal',
            json.dumps(user),
            **headers,
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'message': '회원탈퇴 완료'})