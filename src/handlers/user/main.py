from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram import Bot, types


bot = Bot(token="5341122078:AAEMUVhf-qTogPcNXwheaq9ApYB9BIcglf8")
dp = Dispatcher(bot)


# todo: сделать панельку для команд, сделать токен в самой IDE, сделать загрузку изображений
@dp.message_handler(commands=['start', 'help'])
async def command_start(msg: types.Message):
    try:
        await bot.send_message(msg.from_user.id, 'D (https://t.me/RainOnTues_bot)')
        await msg.delete()
    except:
        await msg.reply('напиши боту (https://t.me/RainOnTues_bot)')


@dp.message_handler(commands=['Режим_работы'])
async def pizza_open_command(msg: types.Message):
    await bot.send_message(msg.from_user.id, 'Вс-Чт с 9:00 до 20:00, Пт-Сб с 10:00 до 23:00')


@dp.message_handler(commands=['Расположение'])
async def pizza_place_command(msg: types.Message):
    await bot.send_message(msg.from_user.id, 'ул. Московская 10')


# @dp.message_handler(commands=['Меню'])
# async def pizza_menu_command(msg: types.Message):
# 	for ret in cur.execute('SELECT * FROM menu').fetchall():
# 	   await bot.send_photo(msg.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')


def register_user_handlers(dp: Dispatcher):
    # todo: register all user handlers
    pass


executor.start_polling(dp, skip_updates=True)
