from database.base import Base
from database.session import engine
from database.models import Weather


def init_db():
    Base.metadata.create_all(engine)
    print("Database initialized")


if __name__ == "__main__":
    init_db()
