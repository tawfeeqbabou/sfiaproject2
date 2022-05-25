from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app


class TestBase(TestCase):
    def create_app(self):
        return app

class TestBook(TestBase):
    def test_richdadpoordad(self):
        with patch('random.randint') as r:
            r.return_value = 0
            response = self.client.get(url_for('get_book'))
            self.assertTrue(b'Rich Dad, Poor Dad', response.data)

    def test_thechimpcomplex(self):
        with patch('random.randint') as r:
            r.return_value = 1
            response = self.client.get(url_for('get_book'))
            self.assertTrue(b'The Chimp Complex', response.data)

    def test_theartofwar(self):
        with patch('random.randint') as r:
            r.return_value = 2
            response = self.client.get(url_for('get_book'))
            self.assertTrue(b'The Art Of War', response.data)


    def test_thirtysecondcode(self):
        with patch('random.randint') as r:
            r.return_value = 3
            response = self.client.get(url_for('get_book'))
            self.assertTrue(b'Thirty Second Code', response.data)