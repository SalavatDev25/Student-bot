from typing import Any

from app.dto.statement import ConvertAnswerDTO, ConvertStatementDTO


class MessageFormatter:
    def create_answer_for_statement(self, cmd: ConvertAnswerDTO):
        department_name = self._create_bold_format(cmd.departament_name)
        title = self._create_bold_format(cmd.message_title)
        message = self._create_bold_format(cmd.message)

        return f"Кафедра: {department_name}\nТема: {title}Сообщение: {message}"

    def create_statement(self, cmd: ConvertStatementDTO) -> str:
        title = self._create_bold_format(cmd.title)
        text = self._create_bold_format(cmd.message)
        user_id = self._create_monospaced_format(cmd.user_id)
        student_name = self._create_bold_format(cmd.name)
        group_number = self._create_bold_format(cmd.group_number)

        return f"Новое обращение от пользователя {user_id}Студент: {student_name}Группа: {group_number}\nЗаголовок обращения: {title}Текст обращения: {text}"

    @staticmethod
    def _create_bold_format(text: Any) -> str:
        return f"*{text}*\n"

    @staticmethod
    def _create_monospaced_format(text: Any) -> str:
        return f"`{text}`\n"
