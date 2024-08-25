import aiogram
from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from aiogram.types import ParseMode

bot = aiogram.Bot(token="7104729744:AAHk9Kf_p4h0kIYfoG2Y2AnZvEBM5RphUpE")
dp = Dispatcher(bot)
@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message("Код на Гитхабе", reply_markup=keyboard)