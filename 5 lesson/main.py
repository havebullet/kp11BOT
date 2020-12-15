import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
import asyncio
from aiogram import Bot, Dispatcher, executor
import csv, datetime
import csv, datetime, pymysql

API_TOKEN = '1227061026:AAH6KOlFyAZRL5PVRcnogTfAHsU1VK1iSes'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(command='start')
async def cmd_start(message: types.Message)
    await message.reply("Привет!")
    statistics(message.chat.id, message.text)
    stat(message.chat.id, message.text)

def stat(user_id, command):
    connection = pymysql.connect('194.58.103.48', 'bot', 'Bot2020', 'bot')
    cursor = connection.cursor()
    data = datetime.datetime.today().strftime("%Y-%m-%d %H:%M")
    cursor.execute("INSERT INTO stat(user_id, user_command, date) VALUES ('%s', '%s', '%s')" % (user_id, command, data))
    connection.commit()
    cursor.close()

def statistics(user_id, command):
    datd = datetime.datetime.today().strftime("%d-%m-%Y %H:%M")
    with open('data.cvs', 'a', newline="") as fil:
        wr = csv.writer(fil, delimiter=';')
        wr.writerow([data, user_id, command])

if __name__ == '__main__':
    executor.start_polling(dp)