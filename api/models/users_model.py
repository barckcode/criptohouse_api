from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String

# Internal Modules
from config.db import meta, engine_postgres


users_table = Table("users", meta,
    Column("id", Integer, primary_key=True, unique=False, nullable=True),
    Column("first_name", String, unique=True, nullable=False),
    Column("last_name", String, unique=True, nullable=False),
    Column("nickname", String, unique=True)
)


meta.create_all(engine_postgres)
