from sqlalchemy import (
    BIGINT,
    Column,
    DateTime,
    ForeignKey,
    String,
    Table,
    Text,
    text,
)

from app.persistent.db_schemas import mapper_registry
from app.persistent.db_schemas.base import APP_SCHEMA

statement_table = Table(
    "statement",
    mapper_registry.metadata,
    Column("id", BIGINT, primary_key=True),
    Column("title", Text, nullable=False),
    Column("message", Text, nullable=False),
    Column("user_id", BIGINT, ForeignKey(f"{APP_SCHEMA}.users.id"), nullable=False),
    Column(
        "departament_id",
        BIGINT,
        ForeignKey(f"{APP_SCHEMA}.departament.id"),
        nullable=False,
    ),
    Column(
        "created_at",
        DateTime(timezone=True),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
    ),
    schema=APP_SCHEMA,
)

user_table = Table(
    "users",
    mapper_registry.metadata,
    Column("id", BIGINT, primary_key=True),
    Column("name", String(255), nullable=True),
    Column("group_number", String(255), nullable=True),
    schema=APP_SCHEMA,
)

departament_table = Table(
    "departament",
    mapper_registry.metadata,
    Column("id", BIGINT, primary_key=True),
    Column("name", String(255), nullable=True),
    schema=APP_SCHEMA,
)
