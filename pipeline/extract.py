import requests


def extract_weather_data():
    # take a city name
    # take query params

    open_meteo_historical_weather_endpoint = (
        "https://archive-api.open-meteo.com/v1/archive"
    )

    params = {
        # sf
        "latitude": 37.7749,
        "longitude": -122.4194,
        # brentwood
        # "latitude": 37.9258,
        # "longitude": -121.6908,
        "start_date": "2025-08-15",
        "end_date": "2025-08-19",
        "hourly": [
            "temperature_2m",
            "apparent_temperature",
            "is_day",
            "relative_humidity_2m",
        ],
        "timezone": "America/Los_Angeles",
    }

    response = requests.get(url=open_meteo_historical_weather_endpoint, params=params)
    response.raise_for_status()
    return response.json()
