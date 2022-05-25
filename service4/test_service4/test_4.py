from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
        def create_app(self):
                return app

class TestResponse(TestBase):
        def test_rich_dad_business(self):
                response = self.client.post(url_for('post_quote'), data = 'Business')
                self.assertTrue(b'Read Rich Dad Poor Dad it will teach you about business', response.data)

        def test_rich_dad_self_improvement(self):
                response = self.client.post(url_for('post_quote'), data = 'Self-improvement')
                self.assertTrue(b'Read Rich Dad Poor Dad it will teach you about self-improvement', response.data)

        def test_rich_dad_strategy(self):
                response = self.client.post(url_for('post_quote'), data = 'Strategy')
                self.assertTrue(b'Read Rich Dad Poor Dad it will teach you about strategy', response.data)

        def test_rich_dad_programming(self):
                response = self.client.post(url_for('post_quote'), data = 'Programming')
                self.assertTrue(b'Read Rich Dad Poor Dad it will teach you about programming', response.data)

        def test_chimp_complex_self_improvement(self):
                response = self.client.post(url_for('post_quote'), data = 'Self-improvement')
                self.assertTrue(b'Read The Chimp Complex it will teach you about self-improvement', response.data)

        def test_chimp_complex_business(self):
                response = self.client.post(url_for('post_quote'), data = 'Business')
                self.assertTrue(b'Read The Chimp Complex it will teach you about business', response.data)

        def test_chimp_complex_strategy(self):
                response = self.client.post(url_for('post_quote'), data = 'Strategy')
                self.assertTrue(b'Read The Chimp Complex it will teach you about strategy', response.data)

        def test_chimp_complex_programming(self):
                response = self.client.post(url_for('post_quote'), data = 'Programming')
                self.assertTrue(b'Read The Chimp Complex it will teach you about programming', response.data)

        def test_art_of_war_strategy(self):
                response = self.client.post(url_for('post_quote'), data = 'Strategy')
                self.assertTrue(b'Read The Art Of War it will teach you about strategy', response.data)

        def test_art_of_war_business(self):
                response = self.client.post(url_for('post_quote'), data = 'Business')
                self.assertTrue(b'Read The Art Of War it will teach you about business', response.data)

        def test_art_of_war_self_improvement(self):
                response = self.client.post(url_for('post_quote'), data = 'Self-improvement')
                self.assertTrue(b'Read The Art Of War it will teach you about self-improvement', response.data)

        def test_art_of_war_programming(self):
                response = self.client.post(url_for('post_quote'), data = 'Programming')
                self.assertTrue(b'Read The Art Of War it will teach you about programming', response.data)

        def test_thirty_second_code_programming(self):
                response = self.client.post(url_for('post_quote'), data = 'Programming')
                self.assertTrue(b'Read Thirty Second Code it will teach you about programming', response.data)

        def test_thirty_second_code_business(self):
                response = self.client.post(url_for('post_quote'), data = 'Business')
                self.assertTrue(b'Read Thirty Second Code it will teach you about business', response.data)

        def test_thirty_second_code_self_improvement(self):
                response = self.client.post(url_for('post_quote'), data = 'Self-improvement')
                self.assertTrue(b'Read Thirty Second Code it will teach you about self-improvement', response.data)

        def test_thirty_second_code_strategy(self):
                response = self.client.post(url_for('post_quote'), data = 'Strategy')
                self.assertTrue(b'Read Thirty Second Code it will teach you about strategy', response.data)