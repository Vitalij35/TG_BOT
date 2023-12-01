from datetime import datetime, timedelta

from aiogram import types, Dispatcher
from aiogram.types import Message


async def mute(message: Message):
    name1 = message.from_user.get_mention(as_html=True)
    if not message.reply_to_message:
        await message.reply("Ця команда повинна бути відповіддю на повідомлення!")
        return
    try:
        muteint = int(message.text.split()[1])
        mutetype = message.text.split()[2]
        comment = " ".join(message.text.split()[3:])
    except IndexError:
        await message.reply('Не достатньо аргументів!\nНаприклад:\n`!mute 1 h причина`')
        return
    if mutetype == "h" or mutetype == "ч" or mutetype == "часів":
        dt = datetime.now() + timedelta(hours=muteint)
        timestamp = dt.timestamp()
        await message.bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id,
                                               types.ChatPermissions(False), until_date=timestamp)
        await message.reply(
            f' | <b>Рішення було принято:</b> {name1}\n | <b>Порушник:</b> <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>\n⏰ | <b>Термін дії:</b> {muteint} {mutetype}\n | <b>Причина:</b> {comment}',
            parse_mode='html')
        await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    elif mutetype == "m" or mutetype == "м" or mutetype == "минут":
        dt = datetime.now() + timedelta(minutes=muteint)
        timestamp = dt.timestamp()
        await message.bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id,
                                               types.ChatPermissions(False), until_date=timestamp)
        await message.reply(
            f' | <b>Рішення було принято:</b> {name1}\n | <b>Порушник:</b> <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>\n⏰ | <b>Термін дії:</b> {muteint} {mutetype}\n | <b>Причина:</b> {comment}',
            parse_mode='html')
        await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    elif mutetype == "d" or mutetype == "д" or mutetype == "днів":
        dt = datetime.now() + timedelta(days=muteint)
        timestamp = dt.timestamp()
        await message.bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id,
                                               types.ChatPermissions(False), until_date=timestamp)
        await message.reply(
            f' | <b>Рішення було принято:</b> {name1}\n | <b>Порушник:</b> <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>\n⏰ | <b>Термін дії:</b> {muteint} {mutetype}\n | <b>Причина:</b> {comment}',
            parse_mode='html')
        await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)


def register_mute(dp: Dispatcher):
    dp.register_message_handler(mute, commands=['mute'], commands_prefix='!/', is_chat_admin=True)
