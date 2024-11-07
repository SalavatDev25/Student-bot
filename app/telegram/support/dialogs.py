from aiogram.enums import ContentType
from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, SwitchTo, Cancel
from aiogram_dialog.widgets.text import Const

from app.telegram.states import FsmSupportChat
from app.telegram.support.handlers import send_support_message_handler, close_dialog_handler

chat_dialog = Dialog(
    Window(
        Const("Отправьте ответ на обращение:"),
        state=FsmSupportChat.OPEN_DIALOG,
    ),
    Window(
        Const("Сообщение отправлено!"),
        MessageInput(send_support_message_handler, content_types=ContentType.ANY),
        Button(Const("Закрыть диалог"), id="back", on_click=close_dialog_handler),
        state=FsmSupportChat.SEND_MESSAGE,
    ),
    Window(
        Const("Диалог закрыт"),
        state=FsmSupportChat.CLOSE_DIALOG,
    ),
)
