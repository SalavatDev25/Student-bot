import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from app.dependences.web_app import WebAppContainer
from app.persistent.db_schemas import init_mappers
from app.settings import Settings
from app.telegram import register


class TelegramBot:
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    @classmethod
    async def start(cls, bot: Bot) -> None:
        register(dp=cls.dp)
        await cls.dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    init_mappers()
    container = WebAppContainer()
    asyncio.run(TelegramBot.start(bot=container.bot()))
