import requests
from django.conf import settings
from django.test import TestCase

# Create your tests here.


class AuthTests(TestCase):
    def test_invalid_params(self):
        data = {
            'username': '123'
        }
        try:
            r = requests.post('http://localhost:8000/api/auth/', json=data, timeout=60)
            json = r.json()
            self.assertTrue(json['error'])
            self.assertEqual(json['status'], 'invalid parameters')
        except requests.Timeout:
            self.fail('timeout')

    def test_user_does_not_exist(self):
        data = {
            'username': 'xXx_lol_i_am_so_random_XD_xXx',
            'password': '123'
        }
        try:
            r = requests.post('http://localhost:8000/api/auth/', json=data, timeout=60)
            json = r.json()
            self.assertTrue(json['error'])
            self.assertEqual(json['status'], 'user does not exist')
        except requests.Timeout:
            self.fail('timeout')

    def test_invalid_password(self):
        data = {
            'username': 'unittest',
            'password': '1234'
        }
        try:
            r = requests.post('http://localhost:8000/api/auth/', json=data, timeout=60)
            json = r.json()
            self.assertTrue(json['error'])
            self.assertEqual(json['status'], 'invalid password')
        except requests.Timeout:
            self.fail('timeout')

    def test_success(self):
        data = {
            'username': 'unittest',
            'password': '123'
        }
        try:
            r = requests.post('http://localhost:8000/api/auth/', json=data, timeout=60)
            json = r.json()
            self.assertFalse(json['error'])
            self.assertEqual(json['status'], 'success')
        except requests.Timeout:
            self.fail('timeout')


class CompilersTests(TestCase):
    def test_compilers(self):
        r = requests.post('http://localhost:8000/api/compilers/', timeout=60)
        json = r.json()
        self.assertFalse(json['error'])
        self.assertEqual(json['compilers'], [c.name for c in settings.COMPILERS])


class PassesTests(TestCase):
    def test_passes(self):
        r = requests.post('http://localhost:8000/api/passes/', timeout=60)
        json = r.json()
        self.assertFalse(json['error'])
        self.assertEqual(json['passes'], [p.name for p in settings.OPS_PASSES])
