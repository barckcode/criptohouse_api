from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import String

# Internal Modules
from config.db import meta, engine_postgres


criptos_table = Table("criptos", meta,
    Column("id", String, primary_key=True, unique=False, nullable=False),
    Column("symbol", String, unique=True, nullable=False),
    Column("name", String, unique=True, nullable=False)
)


meta.create_all(engine_postgres)