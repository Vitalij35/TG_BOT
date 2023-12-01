from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.services.botDB import BotDB


async def my_credits(message: Message):
    if message.reply_to_message:
        credits = BotDB.value(message.reply_to_message.from_user.id)
        await message.bot.send_message(chat_id=message.chat.id, reply_to_message_id=message.reply_to_message.message_id, text=f"Соціальний рейтинг цього☝️: {credits}")
    else:
        credits = BotDB.value(message.from_user.id)
        await message.reply(f"Ваш соціальний рейтинг: {credits}")


def register_my_credits(dp: Dispatcher):
    dp.register_message_handler(my_credits, commands=['my_credits'], commands_prefix="!/")
