from aiogram import Dispatcher
from aiogram.types import Message
from datetime import datetime


async def online_test(message: Message):
    start_datetime = message.bot.get('config').misc.uptime
    start_date = start_datetime.date()
    gpt_calls = message.bot.get('config').misc.gpt_messager

    now_datetime = datetime.now()
    now_date = now_datetime.date()

    up_date = now_date - start_date
    up_time = now_datetime - start_datetime

    await message.delete()
    await message.bot.send_message(chat_id=message.chat.id, text=f"I online!\n\n"
                                                                 f"My uptime: {up_time}\n"
                                                                 f"Chat GPT messages processed: {gpt_calls}!")


def register_online_test(dp: Dispatcher):
    dp.register_message_handler(online_test, commands="online", commands_prefix='!/')
