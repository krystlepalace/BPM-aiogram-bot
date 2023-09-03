from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


router = Router()


@router.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Hello there!\nThis bot can detect BPM from your audio, just send it and results will appear soon!\nFor more help use /help")


@router.message(Command("help"))
async def help_command(message: Message):
    await message.answer("Use this  bot if you need to know BPM of some track quicly and without using specific software or sites.\nJust send audio to the bot and it will detect BPM and send for you.")

