from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


bot = Bot(token="5341122078:AAEMUVhf-qTogPcNXwheaq9ApYB9BIcglf8")
dp = Dispatcher(bot)


@dp.message_handler()
async def echo_send(message: types.Message):
    if message.text == 'привет':
        await message.reply('дарова)')
    if message.text == 'бл"ть':
        await message.reply('удоли')
    # await message.answer(message.text)
    # await message.reply(message.text)
    # await bot.send_message(message.from_user.id, message.text)


def register_other_handlers(dp: Dispatcher) -> None:
    # todo: register all other handlers
    pass
