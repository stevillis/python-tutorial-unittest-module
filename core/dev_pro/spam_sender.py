"""SpamSender module"""


from typing import List, Tuple


def _find_name_from_email(email: str) -> str:
    """Find receiver name in an email and returns it capitalized if found"""
    name_with_dot = email.split('@')[0]
    name_without_dot = name_with_dot.replace('.', ' ')
    return name_without_dot.title()


class EmailChannel:  # pylint: disable=too-few-public-methods
    """Email Chanel class"""

    def send(self, receiver: str, msg: str) -> Tuple[str, str]:  # pylint: disable=no-self-use
        """Send message to receiver"""
        receiver_name = _find_name_from_email(receiver)
        msg_with_receiver_name = f'{receiver_name}, {msg}'
        return receiver, msg_with_receiver_name


class SpamSender:
    """SpamSender class"""

    def __init__(self, receivers: List[str] = None):
        self._receivers = receivers if receivers else []
        self._email_channels = [EmailChannel()]

    @ property
    def receivers(self):
        """Get receivers"""
        return self._receivers

    @ receivers.setter
    def receivers(self, value):
        """Set receivers list"""
        self._receivers = value

    @ property
    def email_channels(self):
        """Get email channels"""
        return self._email_channels

    @ email_channels.setter
    def email_channels(self, value):
        """Set email channels"""
        self.email_channels = value

    def add_receiver(self, receiver: str):
        """Add email receiver to the receivers list"""
        self.receivers.append(receiver)

    def send_spam(self, msg) -> List[Tuple[str, str]]:
        """Method for sending spam"""
        for receiver in self.receivers:
            for channel in self.email_channels:
                yield channel.send(receiver, msg)
