"""Test API simulation modules"""

from unittest import TestCase

from core.api_simulation import facebook, google


class TestAPI(TestCase):
    """Tests for external API"""

    def test_external_api(self):
        """Test external API calls"""
        self.assertEqual(google.call_google_api(), 'data_1')
        self.assertEqual(facebook.call_facebook_api(), 'data_1')
