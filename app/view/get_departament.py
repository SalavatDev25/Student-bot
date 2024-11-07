from sqlalchemy import select

from app.dto.statement import DepartamentDTO
from app.persistent.db_schemas import departament_table
from app.repositories.uow import UnitOfWork


class GetDepartamentView:
    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def __call__(self) -> list[DepartamentDTO]:
        async with self._uow.begin():
            departaments = (
                await self._uow.session.execute(
                    select(departament_table.c.id, departament_table.c.name)
                )
            ).all()

            return [DepartamentDTO(id=d.id, name=d.name) for d in departaments]
