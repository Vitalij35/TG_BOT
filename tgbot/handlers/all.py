from aiogram import Dispatcher
from aiogram.types import Message



async def all(message: Message):
    if not message.reply_to_message:
        await message.reply("Ця команда повинна бути відповіддю на повідомлення!")
        return
    id = message.reply_to_message.message_id

    await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    await message.bot.send_message(message.chat.id, "Якщо начальник сказав (Всіх стосуєтся) чи (всех касается) - то це означає ВСІХ СТОСУЄТСЯ! \nВірно начальник?", reply_to_message_id=id)


def register_all(dp: Dispatcher):
    dp.register_message_handler(all, is_admin=True, commands=["all"], commands_prefix="!/")