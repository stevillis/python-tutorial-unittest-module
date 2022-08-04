"""Test API simulation modules"""

from unittest import TestCase, mock

from core.api_simulation import google


class TestAPI(TestCase):
    """Tests for external API"""

    @mock.patch('core.api_simulation.google.get_data', side_effect=[
        "data_google1",
        "data_google2",
        "data_google3",
    ])
    def test_external_api_mock_setup_tear_down(self, mock_google):
        """Test external API calls with mock"""
        self.assertEqual(google.call_google_api(), 'data_google1')
        self.assertEqual(google.call_google_api(), 'data_google2')
        self.assertEqual(google.call_google_api(), 'data_google3')

    # def setUp(self):
    #     self.patcher = mock.patch(
    #         'core.api_simulation.google.get_data',
    #         return_value='data_google'
    #     )
    #     self.patcher.start()

    # def tearDown(self):
    #     self.patcher.stop()

    # def test_external_api_mock_setup_tear_down(self):
    #     """Test external API calls with mock"""
    #     self.assertEqual(google.call_google_api(), 'data_google')

    # def test_external_api(self):
    #     """Test external API calls"""
    #     self.assertEqual(google.call_google_api(), 'data_1')
    #     self.assertEqual(facebook.call_facebook_api(), 'data_1')

    # def test_external_api(self):
    #     """Test external API calls"""
    #     self.assertEqual(google.call_google_api(), 'data_1')
    #     self.assertEqual(facebook.call_facebook_api(), 'data_1')

    # @mock.patch('core.api_simulation.google.get_data', return_value='data_google')
    # def test_external_api_mock(self, mock_google):
    #     """Test external API calls with mock"""
    #     self.assertEqual(google.call_google_api(), 'data_google')
    #     self.assertEqual(facebook.call_facebook_api(), 'data_1')

    # @mock.patch('core.api_simulation.facebook.get_data', return_value='data_facebook')
    # @mock.patch('core.api_simulation.google.get_data', return_value='data_google')
    # def test_external_api_multiple_mock(self, mock_google, mock_facebook):
    #     """Test external API calls with mock"""
    #     self.assertEqual(google.call_google_api(), 'data_google')
    #     self.assertEqual(facebook.call_facebook_api(), 'data_facebook')

    # def test_external_api_mock_context(self):
    #     """Test external API calls with mock"""
    #     with mock.patch('core.api_simulation.google.get_data', return_value='data_google'):
    #         self.assertEqual(google.call_google_api(), 'data_google')
