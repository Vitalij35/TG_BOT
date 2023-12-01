from aiogram import Dispatcher
from aiogram.types import Message, ContentType

async def resender(message: Message):
    # print(message.chat.id)
    if message.chat.id == -1001831442768:
        await message.forward(chat_id=message.bot.get('config').misc.resend_chat_id)

def register_resender(dp: Dispatcher):
    dp.register_message_handler(resender, content_types=ContentType.ANY)
