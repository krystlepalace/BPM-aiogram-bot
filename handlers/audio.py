from aiogram import Router, F
from aiogram.types import Message
from pathlib import Path
from utils.detecter import Detecter
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

    detecter = Detecter(file_on_disk.__str__())
    bpm = await detecter.detect_bpm()
    key = await detecter.detect_key()

    await message.reply(f"Song: {message.audio.title}\nBPM: {round(bpm[-1], 3)}\nKey: {key}\n\nBy @bpm_detect_bot")

    os.remove(detecter.orig_path)
    os.remove(detecter.converted_path)
