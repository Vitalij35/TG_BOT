from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.services.remove_prefix import remove_prefix


async def ban(message: Message):
    if not message.reply_to_message:
        await message.reply("Ця команда повинна бути відповіддю на повідомлення!")
        return

    await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    await message.bot.kick_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id)

    await message.reply_to_message.reply("Користувача було забанено!\n\nПричина:" + remove_prefix(message.text, "!ban "))

def register_ban(dp: Dispatcher):
    dp.register_message_handler(ban, is_admin=True, commands=["ban"], commands_prefix="!/")