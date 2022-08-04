"""Fake Google API data"""


from core.api_simulation.data import get_data


def call_google_api():
    """Simulates getting data from Google API"""
    data = get_data()
    return data
