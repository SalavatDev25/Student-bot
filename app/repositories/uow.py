import asyncio
from contextlib import asynccontextmanager
from typing import Any, AsyncGenerator, Protocol

from sqlalchemy.ext.asyncio import AsyncSession, async_scoped_session

from app.infrastructure.db import DatabaseSettings, SessionContext
from app.repositories.statement import StatementRepository

from app.repositories.user import UserRepository


class IUnitOfWork(Protocol):
    async def __aenter__(self) -> None:
        ...

    async def __aexit__(self, *args: Any) -> None:
        ...

    async def commit(self) -> None:
        ...

    async def rollback(self) -> None:
        ...


class UnitOfWork(IUnitOfWork):
    def __init__(
        self, database: DatabaseSettings, session_context: SessionContext
    ) -> None:
        self._database = database
        self._session_context = session_context

    @property
    def session(self) -> AsyncSession:
        assert self._session_context.session is not None  # nosec
        return self._session_context.session

    @asynccontextmanager
    async def begin(self) -> AsyncGenerator[AsyncSession, None]:
        scoped_session = None

        if not self._session_context.session:
            scoped_session = async_scoped_session(
                self._database.session_factory,
                asyncio.current_task,
            )
            self._session_context.session = scoped_session()

        if self.session.in_transaction():
            yield self.session
        else:
            try:
                async with self.session.begin():
                    yield self.session
            finally:
                if scoped_session:
                    await scoped_session.remove()
                self._session_context.close_session()

    async def commit(self) -> None:
        await self.session.commit()

    async def rollback(self) -> None:
        await self.session.rollback()

    @property
    def user_repository(self) -> UserRepository:
        return UserRepository(session=self.session)

    @property
    def statement_repository(self) -> StatementRepository:
        return StatementRepository(session=self.session)
