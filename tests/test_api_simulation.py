"""Test API simulation modules"""

from unittest import TestCase, mock

from core.api_simulation import facebook, google


class TestAPI(TestCase):
    """Tests for external API"""

    def test_external_api(self):
        """Test external API calls"""
        self.assertEqual(google.call_google_api(), 'data_1')
        self.assertEqual(facebook.call_facebook_api(), 'data_1')

    @mock.patch('core.api_simulation.google.get_data', return_value='data_google')
    def test_external_api_mock(self, mock_google):
        """Test external API calls with mock"""
        self.assertEqual(google.call_google_api(), 'data_google')
        self.assertEqual(facebook.call_facebook_api(), 'data_1')
