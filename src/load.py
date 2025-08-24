from io import StringIO
import psycopg2
import psycopg2.sql as sql
import pandas as pd


def load_to_db(
    hourly_weather_df: pd.DataFrame, cursor: psycopg2.extensions.cursor, table: str
):
    """Writes given df to a table on given database cursor"""
    # create table if doesnt exist
    create_table_query = sql.SQL("""
        CREATE TABLE IF NOT EXISTS {table} (
            temperature_2m_f REAL,
            apparent_temperature_f REAL,
            uv_index REAL,
            is_day BOOLEAN,
            relative_humidity_2m_perc REAL,
            utc_time TIMESTAMPTZ PRIMARY KEY
        )
    """).format(table=sql.Identifier(table))

    cursor.execute(create_table_query)

    # read df into a csv buffer
    with StringIO() as buffer:
        hourly_weather_df.to_csv(buffer, index=False, header=False)
        buffer.seek(0)

        # copy csv buffer into table
        cursor.copy_from(buffer, table=table, sep=",")
