import pandas as pd
import psycopg2

from src.extract import extract_weather_data
from src.load import load_to_db
from src.transform import transform_weather_data


def main():
    # OPEN_METEO_URL = "https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=37.7749&longitude=-122.4194&start_date=2025-07-16&end_date=2025-08-16&hourly=temperature_2m,apparent_temperature,uv_index,is_day,relative_humidity_2m&timezone=America%2FLos_Angeles&temperature_unit=fahrenheit"
    # raw_data = extract_weather_data(api_url=OPEN_METEO_URL)

    # hourly_weather_df = transform_weather_data(raw_data)

    DB = "weather_db"
    USER = "postgres"
    PASSWORD = "example"
    HOST = "localhost"
    PORT = 5432

    with psycopg2.connect(
        database=DB, user=USER, password=PASSWORD, host=HOST, port=PORT
    ) as conn:
        with conn.cursor() as cur:
            # DB_TABLE = "sf_hourly_weather"
            # load_to_db(hourly_weather_df=hourly_weather_df, cursor=cur, table=DB_TABLE)

            cur.execute("SELECT * FROM sf_hourly_weather")
            # print(pd.DataFrame.from_records(cur.fetchall()))
            print(cur.fetchall())


if __name__ == "__main__":
    main()
