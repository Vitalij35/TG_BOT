import asyncio

from aiogram import Dispatcher
from aiogram.types import Message


async def Lilia_OMG(message: Message):
    print("1")
    new_msg = await message.answer("OMG это случилось! \n\n"
                                   "Древние письмена индейцев майя оказались верны! \n"
                                   "Лиля что-то написала \n"
                                   "Приймите наши поздравления! \n"
                                   "🎉🎉🎉🎉🎉")
    # делайем слип (асинхронно)
    await asyncio.sleep(5)
    # на всякий случай проверяем есть ли еще сообщение
    try:
        await new_msg.delete()
    except Exception as e:
        pass

def register_Lilia(dp: Dispatcher):
    dp.register_message_handler(Lilia_OMG, is_Lilia=True)