import asyncio

from aiogram import Dispatcher
from aiogram.types import Message


async def pentagon(message: Message):
    await message.delete()
    pent = await message.bot.send_message(text="Взлом пентагону розпочався!", chat_id=message.chat.id)

    for i in range(11):
        await pent.edit_text(text=f"Прогрес взлому: {i}0%")
        await asyncio.sleep(1)
        if i == 10:
            await pent.edit_text(text="<u>Пентагон успішно взломаний!</u>\n\n"
                                      ""
                                      "Всі гроші відправлені на альдебаранський рахунок мого боса :)\n"
                                      "<i>P.S. не відкрива двері тим людям</i>")


def register_pentagon(dp: Dispatcher):
    dp.register_message_handler(pentagon, commands="hack", commands_prefix="!/")
