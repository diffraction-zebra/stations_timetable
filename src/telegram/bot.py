import os

from aiogram import Bot
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties


api_token = os.getenv('TELEGRAM_API_TOKEN')
assert api_token

bot = Bot(token=api_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
