from dataclasses import dataclass


@dataclass
class CreateUserCMD:
    id: int
    name: str
    group_number: str


@dataclass
class CreateStatementCMD:
    id: int
    title: str
    message: str
    user_id: int
    departament_id: int


@dataclass
class CreateStatementDTO:
    id: int
    title: str
    message: str
    user_id: int
    name: str
    group_number: str
    departament_id: int


@dataclass
class SendStatementDTO:
    message: str


@dataclass
class DepartamentDTO:
    id: int
    name: str


@dataclass
class GetStatementCMD:
    id: int
    title: str
    user_id: int
    departament_id: int
    departament_name: str


@dataclass
class ConvertStatementDTO:
    id: int
    title: str
    message: str
    user_id: int
    name: str
    group_number: str
    departament_id: int


@dataclass
class ConvertAnswerDTO:
    id: int
    departament_name: str
    message_title: str
    message: str
