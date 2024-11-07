from dataclasses import dataclass
from uuid import UUID

from app.dto.statement import CreateStatementCMD


@dataclass
class Statement:
    id: int
    title: str
    message: str
    user_id: int
    departament_id: int

    @classmethod
    def create(cls, cmd: CreateStatementCMD) -> "Statement":
        return cls(
            id=cmd.id,
            title=cmd.title,
            message=cmd.message,
            user_id=cmd.user_id,
            departament_id=cmd.departament_id,
        )
