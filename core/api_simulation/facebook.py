"""Fake Facebook API data"""


from core.api_simulation.data import get_data


def call_facebook_api():
    """Simulates getting data from Gacebook API"""
    data = get_data()
    return data
