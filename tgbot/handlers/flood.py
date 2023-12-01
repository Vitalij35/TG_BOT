from aiogram.types import Message
from aiogram import dispatcher

from tgbot.services.anti_flood import anti_flood


@dp.throttled(anti_flood, rate=1)
async def flood(message: Message):
    return

