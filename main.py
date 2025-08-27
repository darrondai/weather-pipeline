import pandas as pd
import psycopg2

from src.extract import extract_weather_data
from src.load import load_to_db
from src.transform import transform_weather_data

from database.db import engine


def main():
    raw_data = extract_weather_data()

    hourly_weather_df = transform_weather_data(raw_data)

    load_to_db(hourly_weather_df, engine, "weather")


if __name__ == "__main__":
    main()
