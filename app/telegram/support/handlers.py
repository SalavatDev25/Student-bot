from aiogram import Bot
from aiogram.enums import ParseMode
from aiogram.types import Message, CallbackQuery
from aiogram_dialog import DialogManager
from dependency_injector.wiring import Provide, inject

from app.dependences.web_app import WebAppContainer
from app.dto.statement import ConvertAnswerDTO
from app.telegram.states import FsmSupportChat
from app.utils.converter import MessageFormatter
from app.view.get_statement import GetStatementView


async def open_dialog_with_user(
    callback: CallbackQuery, dialog_manager: DialogManager
) -> None:
    await dialog_manager.start(state=FsmSupportChat.OPEN_DIALOG)
    dialog_manager.dialog_data["statement_id"] = callback.data.replace("st_number:", "")
    await dialog_manager.next()


@inject
async def send_support_message_handler(
    message: Message,
    _,
    dialog_manager: DialogManager,
    bot: Bot = Provide[WebAppContainer.bot],
    message_formatter: MessageFormatter = Provide[WebAppContainer.message_formatter],
    view: GetStatementView = Provide[WebAppContainer.get_statement_view],
) -> None:
    statement = await view(statement_id=dialog_manager.dialog_data["statement_id"])
    dialog_manager.dialog_data["user_id"] = int(statement.user_id)
    message = message_formatter.create_answer_for_statement(
        cmd=ConvertAnswerDTO(
            id=statement.id,
            departament_name=statement.departament_name,
            message_title=statement.title,
            message=message.text
        )
    )
    await bot.send_message(
        chat_id=statement.user_id, text=message, reply_to_message_id=int(statement.id), parse_mode=ParseMode.MARKDOWN
    )


@inject
async def close_dialog_handler(
    callback: CallbackQuery,
    _,
    dialog_manager: DialogManager,
    bot: Bot = Provide[WebAppContainer.bot],
) -> None:
    await bot.send_message(
        chat_id=dialog_manager.dialog_data["user_id"],
        text="Диалог закрыт\nДля отправки нового обращения отправьте боту команду /start"
    )
    await dialog_manager.next()
