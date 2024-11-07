from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from app.telegram.states import FsmMain


async def start_bot_handler(message: Message, dialog_manager: DialogManager) -> None:
    if message:
        await message.delete()
    await dialog_manager.start(FsmMain.MAIN, mode=StartMode.RESET_STACK)
