from typing import Protocol

from sqlalchemy import Select
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.statement import Statement
from app.domain.user import User


class IStatementRepository(Protocol):
    async def save(self, statement: Statement) -> None:
        pass


class StatementRepository(IStatementRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def save(self, statement: Statement) -> None:
        self._session.add(statement)
