from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.services.botDB import BotDB


async def add_to_base(message: Message):
    if not message.reply_to_message:
        if (not BotDB.user_exists(message.from_user.id)):
            BotDB.add_user(message.from_user.id)

        await message.reply("Ви успішно зареєстровані в системі соціального рейтингу!\n"
                            "Партія пишаєтся вами!")
    else:
        if (not BotDB.user_exists(message.reply_to_message.from_user.id)):
            BotDB.add_user(message.reply_to_message.from_user.id)

        await message.bot.send_message(text="Вас успішно зареєстрували в системі соціального рейтингу!\n"
                                            "Партія пишаєтся вами!",
                                       chat_id=message.chat.id, reply_to_message_id=message.reply_to_message.message_id)


def register_add_to_base(dp: Dispatcher):
    dp.register_message_handler(add_to_base, commands=["social"], commands_prefix="!/")
