from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from src.handlers.admin import register_admin_handlers
from src.handlers.user import register_user_handlers
from src.handlers.other import register_other_handlers


def register_all_handlers(dp: Dispatcher):
    handlers = (
        register_user_handlers,
        register_admin_handlers,
        register_other_handlers,
    )
    for handler in handlers:
        handler(dp)
