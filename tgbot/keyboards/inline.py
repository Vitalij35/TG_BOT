from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb = InlineKeyboardMarkup(row_width=2)

ib1 = InlineKeyboardButton(text="Разрешить",
                           callback_data="pass")
ib2 = InlineKeyboardButton(text="Запретить",
                           callback_data="restrict")

ikb.add(ib1, ib2)