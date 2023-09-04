import librosa
import numpy as np
import subprocess
from config import CONFIG

# TODO: make singleton class for opening files with librosa.load
# add method reset() to set instance to None
keys = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#',  'G', 'G#','A', 'A#', 'B']

async def detect_bpm(filepath: str):
    converted_path = f"{filepath.split('.')[0]}.mp3"
    subprocess.run([CONFIG.ffmpeg_path, "-i", filepath, "-vn", "-ar", "44100", "-ac", "2", "-b:a", "192k", converted_path])
    y, sr = librosa.load(converted_path, sr=None)
    bpm = 0
    if y.size != 0:
        bpm = librosa.beat.tempo(y=y, sr=sr) # librosa.feature.rhythm.tempo  in future

    return bpm


async def detect_key(filepath: str):
    converted_path = f"{filepath.split('.')[0]}.mp3"
    subprocess.run(
        [CONFIG.ffmpeg_path, "-i", filepath, "-vn", "-ar", "44100", "-ac", "2",
         "-b:a", "192k", converted_path])
    y, sr = librosa.load(converted_path, sr=None)
    key = None

    chroma = librosa.feature.chroma_cqt(y=y, sr=sr)
    chroma_vals = np.sum(chroma, axis=1)
    most_common_pc = np.argmax(chroma_vals)
    key = keys[most_common_pc-5]

    return key