"""Tests for spam sender"""

import unittest

from core.dev_pro.spam_sender import SpamSender


class SpamSenderTestCase(unittest.TestCase):
    """Tests for SpamSender"""

    def test_create_spam_sender(self):
        """Test SpamSender instance"""
        self.assertIsNotNone(
            SpamSender()
        )  # pyling: ignore=no-value-for-parameter

    def test_spam_sender_has_receivers(self):
        """Test if spam_sender has receivers"""
        receivers = [
            'test1@gmail.com',
            'test2@hotmail.com',
        ]
        spam_sender = SpamSender([receivers[0]])
        self.assertEqual(spam_sender.receivers, [receivers[0]])

        spam_sender.add_receiver(receivers[1])
        self.assertEqual(spam_sender.receivers, receivers)


if __name__ == '__main__':
    unittest.main()
