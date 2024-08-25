import asyncio
import os
import sys
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ParseMode
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

storage = MemoryStorage()
bot = Bot(token=os.environ['7104729744:AAHk9Kf_p4h0kIYfoG2Y2AnZvEBM5RphUpE'])
dp = Dispatcher(bot, storage=storage)
await bot.send_message("Код опубликован в GitHub", chat_id=chat_id)