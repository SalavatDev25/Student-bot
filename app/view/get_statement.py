from sqlalchemy import select

from app.dto.statement import GetStatementCMD
from app.persistent.db_schemas import statement_table, departament_table
from app.repositories.uow import UnitOfWork


class GetStatementView:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def __call__(self, statement_id: str) -> GetStatementCMD:
        async with self._uow.begin():
            query = (
                select(
                    statement_table.c.id,
                    statement_table.c.title,
                    statement_table.c.user_id,
                    statement_table.c.departament_id,
                    departament_table.c.name.label("departament_name"),
                )
                .join(
                    departament_table,
                    statement_table.c.departament_id == departament_table.c.id,
                )
                .where(statement_table.c.id == int(statement_id))
            )

            result = (await self._uow.session.execute(query)).one()

            return GetStatementCMD(
                id=result.id,
                title=result.title,
                user_id=result.user_id,
                departament_id=result.departament_id,
                departament_name=result.departament_name,
            )
