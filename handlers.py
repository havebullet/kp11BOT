# Import library
from main import bot, dp
from aiogram import types
from aiogram.types import Message

# Send message to admin
async def send_to_admin(dp):
	await bot.send_message(chat_id=1190397076, text="Bot start")
