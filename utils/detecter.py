import librosa
import numpy as np
import subprocess
from config import CONFIG


class Detecter:
    def __init__(self, filepath):
        self.keys = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#',  'G', 'G#','A', 'A#', 'B']
        self.orig_path = filepath
        self.converted_path = f"{filepath.split('.')[0]}.mp3"

        subprocess.run(
            [CONFIG.ffmpeg_path, "-i", self.orig_path, "-vn", "-ar", "44100", "-ac",
             "2", "-b:a", "192k", self.converted_path])

        self.loaded_audio = librosa.load(self.converted_path, sr=None)

    async def detect_bpm(self):
        y, sr = self.loaded_audio
        bpm = 0
        if y.size != 0:
            bpm = librosa.beat.tempo(y=y, sr=sr) # librosa.feature.rhythm.tempo  in future

        return bpm

    async def detect_key(self):
        y, sr = self.loaded_audio
        key = None

        chroma = librosa.feature.chroma_cqt(y=y, sr=sr)
        chroma_vals = np.sum(chroma, axis=1)
        most_common_pc = np.argmax(chroma_vals)
        key = self.keys[most_common_pc - 7]

        return key
