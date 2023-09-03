from aiogram import Router, F
from aiogram.types import Message
from pathlib import Path
from utils.detect_bpm import detect
import main
from config import CONFIG


router = Router()


@router.message(F.audio)
async def detect_bpm_reply(message: Message):
    file_id = message.audio.file_id

    file = await main.bot.get_file(file_id)
    file_path = file.file_path
    file_on_disk = Path(f"{CONFIG.media_full_path}{file_id}.mp3")
    
    await main.bot.download_file(file_path, destination=file_on_disk)

    bpm = await detect(file_on_disk.__str__())
    await message.reply(f"Song: {message.audio.title}\nBPM: {round(bpm[-1], 3)}")

