"""Test fs module"""

from unittest import TestCase

from core import fs


class TestFS(TestCase):
    """Tests fs functions"""

    def test_print_contents_of_cwd_success(self):
        """Test print_contents_of_cwd function"""
        actual_result = fs.print_contents_of_cwd()

        expected_directory = b'tests'
        self.assertIn(expected_directory, actual_result)
