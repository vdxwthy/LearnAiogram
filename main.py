import asyncio
from aiogram import Bot, Dispatcher
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

async def main(): 
    await dp.start_polling(bot)
    
    
if __name__ == '__main__':
  asyncio.run(main())