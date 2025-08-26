from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

DB_USER = "postgres"
DB_PASSWORD = "example"
DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "weather_db"

db_url = URL.create(
    drivername="postgresql+psycopg2",
    username=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT,
    database=DB_NAME,
)

engine = create_engine(db_url, echo=True)

SessionLocal = sessionmaker(engine)
