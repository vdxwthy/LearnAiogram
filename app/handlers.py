from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message


router = Router()


@router.message(Command('start'))
async def start(message: Message):
  await message.answer('Hi, this is the bot I use to learn Aiogram v3')
  
  
@router.message(F.text == 'Hello') # You can filter by anything (e.g. F.photo, F.video, F.voice, F.sticker)
async def hello(message: Message):
    await message.answer('Hello! How are you?')