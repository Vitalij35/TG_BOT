from aiogram import Dispatcher
from aiogram.types import Message, ContentType


async def delete_sys_message(message: Message):
    await message.bot.delete_message(message.chat.id, message.message_id)


def register_delete_sys_message(dp: Dispatcher):
    dp.register_message_handler(delete_sys_message,
                                content_types=[ContentType.PINNED_MESSAGE, ContentType.LEFT_CHAT_MEMBER,
                                               ContentType.NEW_CHAT_MEMBERS])
