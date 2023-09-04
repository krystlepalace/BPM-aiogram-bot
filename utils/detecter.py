import librosa
import numpy as np

# TODO: make singleton class for opening files with librosa.load
# add method reset() to set instance to None
keys = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#',  'G', 'G#','A', 'A#', 'B']

async def detect_bpm(filepath: str):
    y, sr = librosa.load(filepath, sr=None)
    bpm = 0
    if y.size != 0:
        bpm = librosa.beat.tempo(y=y, sr=sr) # librosa.feature.rhythm.tempo  in future

    return bpm


async def detect_key(filepath: str):
    y, sr = librosa.load(filepath, sr=None)
    key = None
    chroma = librosa.feature.chroma_cqt(y=y, sr=sr)
     np.sum(chroma, axis=1)