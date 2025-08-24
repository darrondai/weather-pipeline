import requests


def extract_weather_data(api_url: str):
    response = requests.get(url=api_url)
    response.raise_for_status()
    return response.json()
