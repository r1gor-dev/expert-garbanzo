from aiogram.utils import executor
from aiogram import Bot, Dispatcher

from src.handlers import register_all_handlers


async def __on_start_up(dp: Dispatcher) -> None:
    register_all_handlers(dp)


async def on_startup(_):
    print("Bot started.")


def start_bot():
    bot = Bot(token="5341122078:AAEMUVhf-qTogPcNXwheaq9ApYB9BIcglf8")
    dp = Dispatcher(bot)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
