from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.keyboards.inline import ikb


async def added_to_group(message: Message):
    bot_obj = await message.bot.get_me()
    bot_id = bot_obj.id
    for chat_member in message.new_chat_members:
        if chat_member.id == bot_id:
            await message.bot.send_message(chat_id=message.chat.id,text="Халоу\n\n"
                                                                  "Я буду радий працювати тут!\n"
                                                                  "Але є маленький нюанс, мій босс знає що ви мене сюди додали.\n"
                                                                  "Скоріш за все він не дозволить мені тут працювати(\n\n"
                                                                  "<b>Якщо ви не хочете чоб мене звідси видалили звернітся до босса:</b> @Vitalij_technologies")
            message.bot.get('config').misc.restriction_id = message.chat.id
            message.bot.get('config').misc.msg_to_delete = await message.bot.send_message(chat_id=message.bot.get('config').tg_bot.admin_chat,
                                           text=f"Внимание бот был добавлен в группу!\n\n"
                                                f"ID группы: {message.chat.id}\n"
                                                f"Назвние группы: {message.chat.full_name}\n\n"
                                                f"Разрешить боту работать в этой групппе?",
                                           reply_markup=ikb)



def register_added_to_group(dp: Dispatcher):
    dp.register_message_handler(added_to_group, content_types=['new_chat_members'])
