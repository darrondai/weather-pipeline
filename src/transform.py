import pandas as pd


# convert the data into an hourly data frame (or timestamped by time)
# each row is a time, and all of the hourly attributes at that time
def transform_weather_data(response_data: dict) -> pd.DataFrame:
    """Takes an open-meteo api response json in form of a python dict"""

    # load raw response json into dataframe, including meta data
    # each metric is an index, meta data are the columns
    raw_df = pd.DataFrame.from_dict(data=response_data)

    # pivot weather metric lists into column entries
    columns_to_extract = raw_df.index
    hourly_data = {key: raw_df.at[key, "hourly"] for key in columns_to_extract}
    hourly_df = pd.DataFrame(data=hourly_data)

    # parse local time into localized datetime
    hourly_df["time"] = pd.to_datetime(hourly_df["time"])
    original_timezone = raw_df["timezone"]["time"]
    hourly_df["time"] = hourly_df["time"].dt.tz_localize(original_timezone)

    # calc utc_time
    hourly_df["utc_time"] = hourly_df["time"].dt.tz_convert("UTC")

    # drop localized datetime
    hourly_df.drop(columns=["time"], inplace=True)

    return hourly_df
