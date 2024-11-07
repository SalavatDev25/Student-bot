from operator import itemgetter

from aiogram.enums import ContentType
from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Back, Column, Select
from aiogram_dialog.widgets.text import Const, Format

from app.telegram.statement.handlers import (
    input_message_statement_handler,
    input_title_statement_handler,
    input_group_number_handler,
    input_name_handler,
    departament_getter,
    get_departament_handler,
)
from app.telegram.states import FsmStatement
from app.telegram.support.handlers import close_dialog_handler

create_statement_dialog = Dialog(
    Window(
        Const("Выберите кафедру:"),
        Column(
            Select(
                Format("{item[0]}"),
                id="get_department",
                items="departments",
                item_id_getter=itemgetter(1),
                on_click=get_departament_handler,
            )
        ),
        Button(Const("Вернуться"), id="back", on_click=Back()),
        getter=departament_getter,
        state=FsmStatement.SELECT_DEPARTAMENT,
    ),
    Window(
        Const("Укажите свое ФИО:"),
        MessageInput(input_name_handler, content_types=ContentType.TEXT),
        Button(Const("Вернуться"), id="back", on_click=Back()),
        state=FsmStatement.INPUT_FIO,
    ),
    Window(
        Const("Укажите номер группы:"),
        MessageInput(input_group_number_handler, content_types=ContentType.TEXT),
        Button(Const("Вернуться"), id="back", on_click=Back()),
        state=FsmStatement.INPUT_GROUP_NUMBER,
    ),
    Window(
        Const("Укажите заголовок обращения:"),
        MessageInput(input_title_statement_handler, content_types=ContentType.TEXT),
        Button(Const("Вернуться"), id="back", on_click=Back()),
        state=FsmStatement.INPUT_TITLE,
    ),
    Window(
        Const(
            "Внимание! К обращению Вы можете прикрепить фотоизображение при необходимости."
        ),
        Const("Укажите свое обращение:"),
        MessageInput(input_message_statement_handler, content_types=ContentType.ANY),
        Button(Const("Вернуться"), id="back", on_click=Back()),
        state=FsmStatement.INPUT_STATEMENT,
    ),
    Window(
        Format("Ваше обращение зарегистрировано за №{dialog_data[statement_id]}! Ожидайте ответа"),
        MessageInput(input_message_statement_handler, content_types=ContentType.ANY),
        Button(Const("Закрыть диалог"), id="close_chat", on_click=close_dialog_handler),
        state=FsmStatement.SUCCESS,
    ),
)
