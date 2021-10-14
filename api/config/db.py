import os
from sqlalchemy import create_engine, MetaData


USER_DATABASE = os.getenv("DB_USER")
PASSWORD_DATABASE = os.getenv("DB_PASSWORD")
HOST_DATABASE = os.getenv("DB_HOST")
DATABASE = os.getenv("DB_DATABASE")
URL_CONNECTION = f"postgresql://{USER_DATABASE}:{PASSWORD_DATABASE}@{HOST_DATABASE}:5432/{DATABASE}"

meta = MetaData()

engine_postgres = create_engine(URL_CONNECTION)
db_connection = engine_postgres.connect()
