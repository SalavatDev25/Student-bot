from aiogram import Dispatcher
from aiogram.filters import CommandStart
from aiogram_dialog import setup_dialogs

from app.telegram.statement.dialogs import create_statement_dialog
from app.telegram.support.dialogs import chat_dialog
from app.telegram.support.handlers import open_dialog_with_user
from app.telegram.system.dialogs import main_dialog
from app.telegram.system.handlers import start_bot_handler


def register(dp: Dispatcher) -> None:
    dp.include_router(main_dialog)
    dp.include_router(create_statement_dialog)
    dp.include_router(chat_dialog)

    setup_dialogs(dp)

    dp.message.register(
        start_bot_handler,
        CommandStart(),
    )
    dp.callback_query.register(
        open_dialog_with_user, lambda c: c.data and c.data.startswith("st_number:")
    )
