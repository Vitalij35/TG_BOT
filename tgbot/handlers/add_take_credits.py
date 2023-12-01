import re

from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.services.botDB import BotDB


async def record(message: Message):
    if not message.reply_to_message:
        await message.reply("Ця команда повинна бути відповіддю на повідомлення!")
        return

    cmd_variants = (('/-', '/s', '!spent', '!-'), ('/e', '/+', '!e', '!+'))
    operation = '-' if message.text.startswith(cmd_variants[0]) else '+'

    now_credits = BotDB.value(message.reply_to_message.from_user.id)

    value = message.text
    for i in cmd_variants:
        for j in i:
            value = value.replace(j, '').strip()

    if (len(value)):
        x = re.findall(r"\d+(?:.\d+)?", value)

        if (len(x)):
            value = float(x[0].replace(',', '.'))

            if (operation == '-'):
                credits = now_credits - value
                await message.bot.send_message(text=f"Партія обідится на тебе!\n"
                                                    f"Соціальний рейтинг понижено на {value}",
                                               reply_to_message_id=message.reply_to_message.message_id,
                                               chat_id=message.chat.id)
            else:
                credits: int = now_credits + value
                await message.bot.send_message(text=f"Партія пишаєтся тобою!\n"
                                                    f"Соціальний рейтинг підвищено на {value}",
                                               reply_to_message_id=message.reply_to_message.message_id,
                                               chat_id=message.chat.id)

            BotDB.add_record(message.reply_to_message.from_user.id, operation, value)
            BotDB.update_credits(message.reply_to_message.from_user.id, credits)
        else:
            await message.reply("Ти шо там написать, партія не знать твій мисль")
    else:
        await message.reply("Партія не знать скільки рейтинг мінять!")


def register_record(dp: Dispatcher):
    dp.register_message_handler(record, is_admin=True, commands=['s', '-', 'e', '+'],
                                commands_prefix="!/")
