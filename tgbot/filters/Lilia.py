import types
import typing

from aiogram.dispatcher.filters import BoundFilter

from tgbot.config import Config


class IsLiliaFiltter(BoundFilter):
    key = "is_Lilia"

    def __init__(self, is_Lilia: typing.Optional[bool] = None):
        self.is_Lilia = is_Lilia

    async def check(self, obj):
        member = await obj.bot.get_chat_member(obj.chat.id, obj.from_user.id)
        # 827237881 - Lilia, 5265899778 - me
        config: Config = obj.bot.get('config')
        if obj.from_user.id == config.tg_bot.Lilia_id:
            return True