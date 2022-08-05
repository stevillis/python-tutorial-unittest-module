"""Tests for spam sender"""

import unittest
from typing import Tuple

from core.dev_pro.spam_sender import SpamSender


class EmailChannelMock:  # pylint: disable=too-few-public-methods
    """Fake Email channel class"""

    def __init__(self) -> None:
        self._send_method_called = False
        self._send_args = []

    @property
    def send_method_called(self):
        """Getter for send_method_called"""
        return self._send_method_called

    @send_method_called.setter
    def send_method_called(self, value):
        """Setter for send_method_called"""
        self._send_method_called = value

    @property
    def send_args(self):
        """Getter for send_args"""
        return self._send_args

    @send_args.setter
    def send_args(self, value):
        """Setter for send_args"""
        self._send_args = value

    def send(self, receiver: str, msg: str) -> Tuple[str, str]:  # pylint: disable=no-self-use, unused-argument
        """Simulate message sending to receiver"""
        self.send_method_called = True
        self.send_args = [receiver, msg]
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

    def test_email_channel_called(self):
        """Test if mocked email channel was called"""
        spam_sender = SpamSender([self.receivers[0]])
        email_channel_mock = EmailChannelMock()
        spam_sender.email_channels = [
            email_channel_mock
        ]  # dependency injection

        message = 'Lorem ipsum dolor sit amet'
        list(spam_sender.send_spam(message))
        self.assertTrue(email_channel_mock.send_method_called)
        self.assertEqual(email_channel_mock.send_args,
                         [self.receivers[0], message]
                         )


if __name__ == '__main__':
    unittest.main()
