from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram import Router, F
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command
from typing import Dict, Any
from utils.tags_editor import TagsEditor
from pathlib import Path
from config import CONFIG
import main
import os

router = Router()


class ChangeCoverForm(StatesGroup):
    song_name = State()
    song = State()
    cover_image = State()


@router.message(Command("change_cover"))
async def start_change_cover(message: Message, state: FSMContext):
    await state.set_state(ChangeCoverForm.song)
    await message.reply(text="Hi! You want to check cover image of some song? "
                             "Send it to me, and then send image, and I will "
                             "make it!")


async def process_result(message: Message, data: Dict[str, Any]):
    song_file_id = data.get("song")
    cover_file_id = data.get("cover_image")

    file = await main.bot.get_file(song_file_id)
    file_path = file.file_path
    song_on_disk = Path(
        f"{CONFIG.media_full_path}{data.get('song_name')}")
    await main.bot.download_file(file_path, destination=song_on_disk)

    file = await main.bot.get_file(cover_file_id)
    file_path = file.file_path
    cover_on_disk = Path(
        f"{CONFIG.media_full_path}{cover_file_id}.{file_path.split('.')[-1]}")
    await main.bot.download_file(file_path, destination=cover_on_disk)

    editor = TagsEditor(song_on_disk.__str__(), data.get("song_name"))
    await editor.change_cover(cover_on_disk.__str__())

    await main.bot.send_audio(chat_id=message.from_user.id,
                              audio=FSInputFile(song_on_disk.__str__()))

    os.remove(song_on_disk)
    os.remove(cover_on_disk)


@router.message(ChangeCoverForm.song)
async def process_get_song(message: Message, state: FSMContext):
    await state.update_data(song=message.audio.file_id)
    await state.update_data(song_name=message.audio.file_name)
    await state.set_state(ChangeCoverForm.cover_image)
    await message.reply("Great! Now send picture.")


@router.message(ChangeCoverForm.cover_image)
async def process_get_image(message: Message, state: FSMContext):
    data = await state.update_data(cover_image=message.photo[-1].file_id)
    await message.reply("Working on your request! Wait a minute...")

    await process_result(message=message, data=data)
    await state.clear()
