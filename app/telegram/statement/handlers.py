from aiogram import Bot
from aiogram.enums import ParseMode
from aiogram.types import Message, CallbackQuery
from aiogram_dialog import DialogManager
from dependency_injector.wiring import inject, Provide

from app.dependences.web_app import WebAppContainer
from app.dto.statement import CreateStatementDTO
from app.telegram.buttons import create_answer_button
from app.use_case.create_statement import CreateStatementUseCase
from app.view.get_departament import GetDepartamentView


@inject
async def departament_getter(
    view: GetDepartamentView = Provide[WebAppContainer.get_departament_view], **kwargs
) -> dict:
    return {
        "departments": [(f"{d.name}", d.id) for d in await view()],  # type: ignore
    }


async def get_departament_handler(
    callback: CallbackQuery, _, dialog_manager: DialogManager, departament_id: str
) -> None:
    dialog_manager.dialog_data["departament_id"] = int(departament_id)
    await dialog_manager.next()


async def input_name_handler(
    message: Message, _, dialog_manager: DialogManager
) -> None:
    dialog_manager.dialog_data["student_name"] = message.text
    await dialog_manager.next()


async def input_group_number_handler(
    message: Message, _, dialog_manager: DialogManager
) -> None:
    dialog_manager.dialog_data["group_number"] = message.text
    await dialog_manager.next()


async def input_title_statement_handler(
    message: Message, _, dialog_manager: DialogManager
) -> None:
    dialog_manager.dialog_data["title_statement"] = message.text
    await dialog_manager.next()


@inject
async def input_message_statement_handler(
    message: Message,
    _,
    dialog_manager: DialogManager,
    bot: Bot = Provide[WebAppContainer.bot],
    use_case: CreateStatementUseCase = Provide[
        WebAppContainer.create_statement_use_case
    ],
) -> None:
    dialog_manager.dialog_data["statement_id"] = message.message_id

    result = await use_case(
        cmd=CreateStatementDTO(
            id=dialog_manager.dialog_data["statement_id"],
            title=dialog_manager.dialog_data["title_statement"],
            message=message.text,
            user_id=message.from_user.id,
            name=dialog_manager.dialog_data["student_name"],
            group_number=dialog_manager.dialog_data["group_number"],
            departament_id=dialog_manager.dialog_data["departament_id"],
        )
    )
    await bot.send_message(
        chat_id=dialog_manager.dialog_data["departament_id"],
        text=result.message,
        reply_markup=create_answer_button(statement_id=message.message_id),
        parse_mode=ParseMode.MARKDOWN,
    )
    await dialog_manager.next()
