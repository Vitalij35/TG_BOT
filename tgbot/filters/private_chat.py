import typing
from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class private_filter(BoundFilter):
    key = 'is_private'

    def __init__(self, is_private: typing.Optional[bool] = None):
        self.is_private = is_private

    async def check(self, obj):
        if self.is_private is None:
            return False
        return obj.chat.type == types.ChatType.PRIVATE