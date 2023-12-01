from aiogram import Dispatcher
from aiogram.types import Message


async def start(message: Message):
    await message.bot.send_message(message.chat.id, "Привіт!\n\n"
                                                    "Я - бот розроблений як адміністратор группи, але основна моя фішка -- інтегрована нейромережа.\n"
                                                    "Все керування ботом є в меню, час обробки запиті може сягати 3хв у випадку довгих текстів! Всі запити рекомендую формулювати максимально точно.\n\n"
                                                    "У випадку питань/скарг/пропозицій звертайтеся до мого розробника -- @Vitalij_technologies")

def register_start(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start"], commands_prefix="!/")