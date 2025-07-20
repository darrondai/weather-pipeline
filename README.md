# weather-pipeline

A basic ETL pipeline that pulls data from https://open-meteo.com, transforms the JSON response into a Pandas DataFrame and loads into a PostgreSQL database.

## How to run:

1. `git clone` the repo and then `cd` into it
2. `python3 -m venv .venv` to initialize virtual env
3. `source .venv/bin/activate` to activate virtual env
4. `pip install -r requirements.txt` to install python project dependencies
5. `docker compose up -d` to run postgres database headlessly
6. `python main.py` to run pipeline
7. `docker compose down` to shutdown database and network
