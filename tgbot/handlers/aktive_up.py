import asyncio
from apscheduler import AsyncIOScheduler
from aiogram import Dispatcher
from aiogram.types import Message
from datetime import datetime


async def send(message: Message):
    await message.bot.send_message(message.bot.get('config').misc.deafoult_chat_id, f"Тест автоматичної розсилки повідомлень...\n"
                                                                                        f"Не звертайте уваги")

async def shelduer():
    scheduler.add_job(send, 'cron', day_of_week='mon-sun', hour=19, minute=22, end_date='2025-10-13')
    scheduler.start()