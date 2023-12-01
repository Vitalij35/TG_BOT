
import psutil as psutil
from aiogram import Dispatcher
from aiogram.types import Message


async def ping(message: Message):
    # Check if command is sent by group admin
    user = await message.bot.get_chat_member(message.chat.id, message.from_user.id)
    if user.is_chat_admin():
        ram = psutil.virtual_memory()

        reply = "👊 Up & Running!\n\n"
        reply += "CPU: " + str(psutil.cpu_count()) + " cores (" + str(
            psutil.cpu_freq().max) + "MHz) with " + str(psutil.cpu_percent()) + "% current usage\n"
        reply += "RAM: " + str(ram.used >> 20) + "mb / " + str(ram.total >> 20) + "mb\n";

        reply += "\nBot version: " + str("2.5") + " codename: «" + "VTB" + "» 🌚"

        await message.bot.send_message(chat_id=message.chat.id, text=reply)
        await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)


def register_ping(dp: Dispatcher):
    dp.register_message_handler(ping, commands="ping", commands_prefix="!/")