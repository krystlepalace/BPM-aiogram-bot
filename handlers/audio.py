from aiogram import Router, F
from aiogram.types import Message


router = Router()


@router.message(F.audio)
async def detect_bpm_reply(message: Message):
    await message.reply("BPM: ")

