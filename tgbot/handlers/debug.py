from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.services.remove_prefix import remove_prefix


async def debug(message: Message):
    print(message.chat.id)
    await message.bot.send_message(chat_id=message.chat.id, text=f"Id: {message.chat.id}")


def register_debug(dp: Dispatcher):
    dp.register_message_handler(debug)