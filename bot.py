import asyncio
import logging
from datetime import datetime

import openai as openai
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram.types import CallbackQuery

from tgbot.config import load_config
from tgbot.filters.Lilia import IsLiliaFiltter
from tgbot.filters.admin import AdminFilter
from tgbot.filters.private_chat import private_filter
from tgbot.handlers.GPT import register_gpt_global, register_gpt_personal
# from tgbot.handlers.Lilia_OMG import register_Lilia
from tgbot.handlers.resender import register_resender
from tgbot.handlers.Pentagon import register_pentagon
from tgbot.handlers.add_to_group import register_added_to_group
from tgbot.handlers.all import register_all
from tgbot.handlers.ban import register_ban
from tgbot.handlers.message_from_bot import register_msg
from tgbot.handlers.mute import register_mute
from tgbot.handlers.native_unmute import register_native_unmute
from tgbot.handlers.online_test import register_online_test
from tgbot.handlers.ping import register_ping
from tgbot.handlers.system_messages_deleter import register_delete_sys_message
from tgbot.handlers.weather import register_weather
from tgbot.middlewares.environment import EnvironmentMiddleware
from tgbot.handlers.new_member_to_DB import register_add_to_base
from tgbot.handlers.add_take_credits import register_record
from tgbot.handlers.my_credits import register_my_credits
from tgbot.handlers.start import register_start
from tgbot.handlers.aktive_up import shelduer

logger = logging.getLogger(__name__)


def register_all_middlewares(dp, config):
    dp.setup_middleware(EnvironmentMiddleware(config=config))


def register_all_filters(dp):
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(IsLiliaFiltter)
    dp.filters_factory.bind(private_filter)


def register_all_handlers(dp):
    register_start(dp)
    register_all(dp)
    register_ping(dp)
    register_msg(dp)
    register_added_to_group(dp)
    register_ban(dp)
    register_mute(dp)
    register_native_unmute(dp)
    register_online_test(dp)
    register_weather(dp)
    register_delete_sys_message(dp)
    register_pentagon(dp)

    register_add_to_base(dp)
    register_my_credits(dp)
    register_record(dp)

    register_gpt_global(dp)
    register_gpt_personal(dp)

    # register_Lilia(dp)
    register_resender(dp)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")
    config = load_config(".env")

    storage = RedisStorage2() if config.tg_bot.use_redis else MemoryStorage()
    # bot = Bot(token=config.tg_bot.token, parse_mode='HTML', proxy=config.tg_bot.proxy)
    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher(bot, storage=storage)

    bot['config'] = config

    openai.api_key = bot.get('config').misc.openAI_token

    register_all_middlewares(dp, config)
    register_all_filters(dp)
    register_all_handlers(dp)

    admin_chat = bot.get('config').tg_bot.admin_chat

    @dp.callback_query_handler()
    async def restrict(callback: CallbackQuery):
        if callback.data == "restrict":
            await bot.get('config').misc.msg_to_delete.delete()
            await bot.send_message(chat_id=admin_chat,
                                   text=f"Сер, вы успешно запретили мне работать в группе "
                                        f"{bot.get('config').misc.restriction_id}")
            await bot.send_message(chat_id=bot.get('config').misc.restriction_id,
                                   text="Извените но начальник не одобряет мое нахождение в этой группе!")
            await bot.leave_chat(chat_id=bot.get('config').misc.restriction_id)
        elif callback.data == "pass":
            await bot.get('config').misc.msg_to_delete.delete()
            await bot.send_message(chat_id=admin_chat,
                                   text=f"Сер, спасибо вам за то что вы разрешили мне работать в группе "
                                        f"{bot.get('config').misc.restriction_id}")
            await bot.send_message(chat_id=bot.get('config').misc.restriction_id,
                                   text="Мой начальник разрешил мне работать здесь!")

    # start
    try:
        bot.get('config').misc.uptime = datetime.now()
        await bot.send_message(chat_id=admin_chat, text="Bot is now online!")
        asyncio.create_task(shelduer())
        await dp.start_polling()
    finally:
        await bot.send_message(chat_id=admin_chat, text="Bot offline!")
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
