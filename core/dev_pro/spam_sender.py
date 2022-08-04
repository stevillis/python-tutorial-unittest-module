"""SpamSender module"""


from typing import List, Optional


class SpamSender:
    """SpamSender class"""

    def __init__(self, receivers: Optional[List[str]] = None):
        self._receivers = receivers

    @property
    def receivers(self):
        """Get SpamSender receivers"""
        return self._receivers

    @receivers.setter
    def receivers(self, value):
        """Add email receiver to the receivers list"""
        self._receivers = value

    def add_receiver(self, receiver: str):
        """Add email receiver to the receivers list"""
        self.receivers.append(receiver)
