from aiogram import Bot, Dispatcher
from aiogram.utils import executor

API_TOKEN = '7104729744:AAHk9Kf_p4h0kIYfoG2Y2AnZvEBM5RphUpE'
CHAT_ID = '5079152888'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

async def on_startup(dispatcher: Dispatcher):
    # Отправляем сообщение при запуске
    await bot.send_message(CHAT_ID, "Код на Гитхабе")

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
