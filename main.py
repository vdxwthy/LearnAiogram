import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv
import os
load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command('start'))
async def start(message: Message):
  await message.answer('Hi, this is the bot I use to learn Aiogram v3')
  
  
@dp.message(F.text == 'Hello') # You can filter by anything (e.g. F.photo, F.video, F.voice, F.sticker)
async def hello(message: Message):
    await message.answer('Hello! How are you?')

async def main(): 
    await dp.start_polling(bot)
       
if __name__ == '__main__':
  asyncio.run(main())