from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import String

# Internal Modules
from config.db import meta, engine_postgres


currencies_table = Table("currencies", meta,
    Column("id", String, primary_key=True, unique=False, nullable=True),
    Column("symbol", String, unique=True, nullable=False),
    Column("name", String, unique=True, nullable=False)
)


meta.create_all(engine_postgres)
