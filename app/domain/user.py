from dataclasses import dataclass

from app.dto.statement import CreateUserCMD


@dataclass
class User:
    id: int
    name: str
    group_number: str

    @classmethod
    def create(cls, cmd: CreateUserCMD) -> "User":
        return cls(id=cmd.id, name=cmd.name, group_number=cmd.group_number)
