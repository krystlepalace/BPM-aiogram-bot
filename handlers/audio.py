from aiogram import Router, F
from aiogram.types import Message
from pathlib import Path
from utils.detecter import detect_bpm, detect_key
import main
from config import CONFIG
import os


router = Router()


@router.message(F.audio)
async def detect_bpm_reply(message: Message):
    await message.reply("Wait a minute...")
    file_id = message.audio.file_id

    file = await main.bot.get_file(file_id)
    file_path = file.file_path
    file_on_disk = Path(f"{CONFIG.media_full_path}{file_id}.{file_path.split('.')[-1]}")
    
    await main.bot.download_file(file_path, destination=file_on_disk)

    bpm = await detect_bpm(file_on_disk.__str__())
    key = await detect_key(file_on_disk.__str__())

    await message.reply(f"Song: {message.audio.title}\nBPM: {round(bpm[-1], 3)}\nKey: {key}\n\nBy @bpm_detect_bot")
    os.remove(file_on_disk)
    os.remove(Path(f"{file_on_disk.__str__().split('.')[0]}.mp3"))
