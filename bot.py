import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token='6053665361:AAGToiVSGf_p2zx5lhPk_z9w78juUJabKX4')
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message):
    await message.reply("Бот-переводчик с Deepl. Отправьте мне текст на английском, я переведу его на русский.")


@dp.message_handler()
async def translate(message):
    text = message.text
    translation = await translate_text(text)
    await message.reply(translation)


async def translate_text(text):
    url = "https://api-free.deepl.com/v2/translate"
    params = {
        "auth_key": 'XXXXXXXXXXXXXXXXXXXX',
        "text": text,
        "target_lang": "RU"
    }

    response = requests.post(url, params=params)
    data = response.json()
    translation = data["translations"][0]["text"]
    return translation

executor.start_polling(dp, skip_updates=True)