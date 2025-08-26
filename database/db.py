from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass

# TODO: use env variables in the future
# database login credential constants
DB_USER = "postgres"
DB_PASSWORD = "example"
DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "weather_db"

# programatically create database url
db_url = URL.create(
    drivername="postgresql+psycopg2",
    username=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT,
    database=DB_NAME,
)

# create engine which will be shared across all db operations
engine = create_engine(db_url, echo=True)

# create sessionmaker which will be shared across all db operations
SessionLocal = sessionmaker(engine)


# define base class for other models, declarative and mapped as dataclass
class Base(DeclarativeBase, MappedAsDataclass):
    """Base class for ORM models"""

    pass
