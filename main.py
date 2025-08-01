import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv
import os

from app.handlers import router
load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()
async def main(): 
  dp.include_router(router)
  await dp.start_polling(bot)
       
if __name__ == '__main__':
  asyncio.run(main())