from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app



class TestBase(TestCase):
    def create_app(self):
        return app

class TestCase(TestBase):
    def test_business(self):
        with patch('random.randint') as r:
            r.return_value = 0
            response = self.client.get(url_for('get_genre'))
            self.assertIn(b'Business', response.data)

    def test_self_improvement(self):
        with patch('random.randint') as r:
            r.return_value = 1
            response = self.client.get(url_for('get_genre'))
            self.assertIn(b'Self-improvement', response.data)

    def test_strategy(self):
        with patch('random.randint') as r:
            r.return_value = 2
            response = self.client.get(url_for('get_genre'))
            self.assertIn(b'Strategy', response.data)


    def test_programming(self):
        with patch('random.randint') as r:
            r.return_value = 3
            response = self.client.get(url_for('get_genre'))
            self.assertIn(b'Programming', response.data)