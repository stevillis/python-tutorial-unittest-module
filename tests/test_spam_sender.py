"""Tests for spam sender"""

import unittest
from typing import Tuple

from core.dev_pro.spam_sender import SpamSender


class EmailChannelMock:  # pylint: disable=too-few-public-methods
    """Fake Email channel class"""

    def send(self, receiver: str, msg: str) -> Tuple[str, str]:  # pylint: disable=no-self-use, unused-argument
        """Simulate message sending to receiver"""
        return 'john.cena@gmail.com', 'John Cena, Lorem ipsum dolor sit amet'


class SpamSenderTestCase(unittest.TestCase):
    """Tests for SpamSender"""

    @classmethod
    def setUpClass(cls):
        cls.receivers = [
            'john.cena@gmail.com',
            'dua.lipa@hotmail.com',
        ]

    def test_create_spam_sender(self):
        """Test SpamSender instance"""
        self.assertIsNotNone(
            SpamSender()
        )  # pyling: ignore=no-value-for-parameter

    def test_spam_sender_has_receivers(self):
        """Test if spam_sender has receivers"""
        spam_sender = SpamSender([self.receivers[0]])
        self.assertEqual(spam_sender.receivers, [self.receivers[0]])

        spam_sender.add_receiver(self.receivers[1])
        self.assertEqual(spam_sender.receivers, self.receivers)

    def test_send_spam(self):
        """Test spam sending"""
        spam_sender = SpamSender([self.receivers[0]])
        spam_sender.email_channels = [
            EmailChannelMock()
        ]  # dependency injection
        expected_result = [
            (self.receivers[0], 'John Cena, Lorem ipsum dolor sit amet'),
        ]
        self.assertEqual(
            list(spam_sender.send_spam('Lorem ipsum dolor sit amet')),
            expected_result
        )


if __name__ == '__main__':
    unittest.main()
