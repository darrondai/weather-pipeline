import pandas as pd


# convert the data into an hourly data frame (or timestamped by time)
# each row is a time, and all of the hourly attributes at that time
def transform_weather_data(response_data: dict) -> pd.DataFrame:
    flattened_df = pd.json_normalize(data=response_data)

    hourly_data = {
        key: flattened_df.loc[0, key]
        for key in flattened_df.columns
        if "hourly." in key
    }

    # put latitude, longitude in each hourly data point
    hourly_data["latitude"] = flattened_df.loc[0, "latitude"]
    hourly_data["longitude"] = flattened_df.loc[0, "longitude"]

    hourly_df = pd.DataFrame.from_dict(hourly_data)

    # rename flattened columns strip 'hourly.' prefix, add units to column names
    hourly_df = hourly_df.rename(
        columns={
            "hourly.temperature_2m": "temperature_2m_f",
            "hourly.time": "local_time",
            "hourly.apparent_temperature": "apparent_temperature_f",
            "hourly.is_day": "is_day",
            "hourly.relative_humidity_2m": "relative_humidity_2m_perc",
        }
    )

    # ENFORCE DATA TYPES AFTER LOADING
    DTYPE_MAP = {
        "latitude": float,
        "longitude": float,
        "is_day": bool,
        "temperature_2m_f": float,
        "apparent_temperature_f": float,
        "relative_humidity_2m_perc": int,
    }
    hourly_df = hourly_df.astype(DTYPE_MAP)

    # convert time strings to datetimes with timezone awareness
    original_timezone = flattened_df.loc[0, "timezone"]

    # parse time string into datetime, then make it timezone aware of the original timezone
    hourly_df["local_time"] = pd.to_datetime(hourly_df["local_time"]).dt.tz_localize(
        original_timezone
    )

    # calc utc_time
    hourly_df["utc_time"] = hourly_df["local_time"].dt.tz_convert("UTC")

    return hourly_df
