from abc import abstractmethod
from typing import Protocol

from sqlalchemy import Select
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.user import User


class IUserRepository(Protocol):
    @abstractmethod
    async def get_user(self, user_id: int) -> User | None:
        raise NotImplementedError

    @abstractmethod
    async def save(self, user: User) -> None:
        raise NotImplementedError


class UserRepository(IUserRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_user(self, user_id: int) -> User | None:
        stmt = Select(User).filter_by(id=user_id)
        user = (await self._session.execute(stmt)).scalar()
        return user

    async def save(self, user: User) -> None:
        self._session.add(user)
