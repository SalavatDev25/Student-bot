import logging

from app.domain.statement import Statement
from app.domain.user import User
from app.dto.statement import (
    CreateStatementDTO,
    SendStatementDTO,
    CreateUserCMD,
    CreateStatementCMD, ConvertStatementDTO,
)
from app.repositories.uow import UnitOfWork
from app.utils.converter import MessageFormatter


class CreateStatementUseCase:
    def __init__(self, formatter: MessageFormatter, uow: UnitOfWork):
        self._formatter = formatter
        self._uow = uow

    async def __call__(self, cmd: CreateStatementDTO) -> SendStatementDTO:
        async with self._uow.begin():
            user = await self._uow.user_repository.get_user(user_id=cmd.user_id)

            if user is None:
                user = User.create(
                    cmd=CreateUserCMD(
                        id=cmd.user_id, name=cmd.name, group_number=cmd.group_number
                    )
                )
                await self._uow.user_repository.save(user)

            statement = Statement.create(
                cmd=CreateStatementCMD(
                    id=cmd.id,
                    title=cmd.title,
                    message=cmd.message,
                    user_id=cmd.user_id,
                    departament_id=cmd.departament_id,
                )
            )

            formated_statement = self._formatter.create_statement(
                cmd=ConvertStatementDTO(
                    id=statement.id,
                    title=statement.title,
                    message=cmd.message,
                    user_id=cmd.user_id,
                    name=user.name,
                    group_number=user.group_number,
                    departament_id=statement.departament_id
                )
            )
            await self._uow.statement_repository.save(statement)
            return SendStatementDTO(message=formated_statement)
