import pandas as pd
from sqlalchemy.engine import Connectable


def load_to_db(
    df: pd.DataFrame, con: Connectable, table: str, if_exists: str = "append"
):
    df.to_sql(name=table, con=con, if_exists=if_exists, index=False)
