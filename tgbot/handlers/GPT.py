import openai
from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher.filters import filters

from tgbot.services.remove_prefix import remove_prefix

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": 'Translate the following English text to French: "{text}"'},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
]


def update(message, role, content):
    messages.append({"role": role, "content": content})
    return message

async def gpt_global(message: Message):
    calls = message.bot.get('config').misc.gpt_messager
    message.bot.get('config').misc.gpt_messager = calls + 1

    update(messages, "user", remove_prefix(message.text, "@Vitalij_Techologies_Bot"))
    respounse = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    await message.answer(respounse['choices'][0]['message']['content'])

async def gpt_personal(message: Message):
    calls = message.bot.get('config').misc.gpt_messager
    message.bot.get('config').misc.gpt_messager = calls+1

    if '@Vitalij_Techologies_Bot' in message.text:
        update(messages, "user", remove_prefix(message.text, "@Vitalij_Techologies_Bot "))
    else:
        update(messages, "user", message.text)

    respounse = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    await message.answer(respounse['choices'][0]['message']['content'])
def register_gpt_global(dp: Dispatcher):
    dp.register_message_handler(gpt_global, commands="Vitalij_Techologies_Bot", commands_prefix="@")

def register_gpt_personal(dp: Dispatcher):
    dp.register_message_handler(gpt_personal, is_private=True)