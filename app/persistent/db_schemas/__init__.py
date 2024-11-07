from sqlalchemy.orm import relationship

from app.domain.departament import Departament
from app.domain.statement import Statement
from app.domain.user import User
from app.persistent.db_schemas.base import mapper_registry
from app.persistent.db_schemas.statement import (
    user_table,
    statement_table,
    departament_table,
)


def init_mappers() -> None:
    mapper_registry.map_imperatively(
        User,
        user_table,
        properties={
            "statement": relationship(
                Statement,
            )
        },
    )

    mapper_registry.map_imperatively(
        Departament,
        departament_table,
        properties={
            "statement": relationship(
                Statement,
            )
        },
    )

    mapper_registry.map_imperatively(
        Statement,
        statement_table,
        properties={
            "users": relationship(
                User,
            ),
            "departament": relationship(Departament),
        },
    )
