"""Test fs module"""

from unittest import TestCase, mock

from core import fs


class TestFS(TestCase):
    """Tests fs functions"""

    def test_print_contents_of_cwd_success(self):
        """Test print_contents_of_cwd function"""
        actual_result = fs.print_contents_of_cwd()

        expected_directory = b'tests'
        self.assertIn(expected_directory, actual_result)

    @mock.patch('core.fs.check_output', return_value=b'foo\nbar\n')
    def test_print_contents_of_cwd_success_with_mocking(self, mock_check_output):
        """Test print_contents_of_cwd function"""
        actual_result = fs.print_contents_of_cwd()

        expected_directory = b'foo'
        self.assertIn(expected_directory, actual_result)
