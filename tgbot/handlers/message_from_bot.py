from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.services.remove_prefix import remove_prefix


async def message_from_bot(message: Message):
    global msg_noPefix
    if '!msg ' in message.text:
        msg_noPefix = remove_prefix(message.text, "!msg ")
    elif '/msg ' in message.text:
        msg_noPefix = remove_prefix(message.text, "/msg ")
    elif '/msg@Vitalij_Techologies_Bot ' in message.text:
        msg_noPefix = remove_prefix(message.text, "/msg@Vitalij_Techologies_Bot ")

    if message.reply_to_message:
        await message.bot.send_message(message.chat.id, msg_noPefix, reply_to_message_id=message.reply_to_message)
    else:
        await message.bot.send_message(message.chat.id, msg_noPefix)
    await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)


def register_msg(dp: Dispatcher):
    dp.register_message_handler(message_from_bot, commands=["msg"], commands_prefix="!/")
