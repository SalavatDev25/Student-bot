from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button, Start
from aiogram_dialog.widgets.text import Const

from app.telegram.states import (
    FsmMain,
    FsmStatement,
)

main_dialog = Dialog(
    Window(
        Const(
            "Добро пожаловать! Для направления своего обращение нажмите на кнопку 'Создать новое обращение'"
        ),
        Button(
            Const("Создать новое обращение"),
            id="create_message",
            on_click=Start(
                Const("Create statement"),
                id="create_statement",
                state=FsmStatement.SELECT_DEPARTAMENT,
            ),
        ),
        state=FsmMain.MAIN,
    ),
)
