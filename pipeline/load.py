import pandas as pd
from sqlalchemy.engine import Engine
from database.models import Weather
from sqlalchemy.dialects.postgresql import insert


def load_to_db(df: pd.DataFrame, engine: Engine, table: str):
    """Append the given dataframe into the corresponding database table. On primary key conflict, do nothing."""

    records = df.to_dict(orient="records")
    stmt = insert(Weather).values(records).on_conflict_do_nothing()

    with engine.begin() as conn:
        conn.execute(stmt)
