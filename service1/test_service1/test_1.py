from flask import url_for
from unittest.mock import patch
from flask_testing import TestCase
from application import app

class unittesting(TestCase):
    def create_app(self):
        return app


class TestResponse(unittesting):
    def test_book(self):
        with patch("requests.get") as g:
            with patch("requests.post") as p:
                g.return_value.text = "Those who master money, master life"
                p.return_value.text = "It is better to be a warrior in the garden, than a gardner in war"
                response = self.client.get(url_for('get_book'))
                self.assertIn(b'Those who master money, master life', response.data)
                self.assertIn(b'It is better to be a warrior in the garden, than a gardner in war', response.data)