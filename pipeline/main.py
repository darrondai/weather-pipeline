from pipeline.extract import extract_weather_data
from pipeline.load import load_to_db
from pipeline.transform import transform_weather_data

from database.db import engine


def main():
    # Step 1: Extract
    raw_data = extract_weather_data()

    # Step 2: Transform
    hourly_weather_df = transform_weather_data(raw_data)

    # Step 3: Load
    load_to_db(hourly_weather_df, engine, "weather")


if __name__ == "__main__":
    main()
