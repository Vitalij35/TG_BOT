from datetime import datetime, timedelta

from aiogram import Dispatcher, types
from aiogram.types import Message


async def native_unmute(message: Message):
    if not message.reply_to_message:
        await message.reply("Ця команда повинна бути відповіддю на повідомлення!")
        return

    dt = datetime.now() + timedelta(minutes=1)
    timestamp = dt.timestamp()
    await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    await message.bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False),
                                   until_date=timestamp)
    await message.reply_to_message.reply("Користувача буде розмучено через 1 хвилину!")

def register_native_unmute(dp: Dispatcher):
    dp.register_message_handler(native_unmute, is_admin=True, commands=["unmute"], commands_prefix="!/")