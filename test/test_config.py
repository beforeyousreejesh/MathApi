import unittest

from flask import current_app
from flask_testing import TestCase


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        current_app.config.from_object('main.config.DevelopmentConfig')
        return current_app
    def test_app_is_development(self):
        self.assertFalse(current_app is None)
        self.assertTrue(current_app.config['SECRET_KEY'] is 'great_secret_key')
        self.assertTrue(current_app.config['DEBUG'] is True)

class TestProductionConfig(TestCase):
    def create_app(self):
        current_app.config.from_object('main.config.ProductionConfig')
        return current_app
    def test_app_is_production(self):
        self.assertFalse(current_app is None)
        self.assertTrue(current_app.config['SECRET_KEY'] is 'great_secret_key')
        self.assertTrue(current_app.config['DEBUG'] is False)