from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String

# Internal Modules
from config.db import meta, engine_postgres


preferences_currencies_table = Table("preferences_currencies", meta,
    Column("id", Integer, primary_key=True, autoincrement=True, unique=True, nullable=False),
    Column("id_user", Integer, unique=True, nullable=False),
    Column("id_currency", String, nullable=False)
)


meta.create_all(engine_postgres)
