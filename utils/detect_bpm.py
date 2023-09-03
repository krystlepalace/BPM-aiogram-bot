import librosa


async def detect(filepath: str):
    y, sr = librosa.load(filepath, sr=None)
    bpm = 0
    if y.size != 0:
        bpm = librosa.beat.tempo(y=y, sr=sr)

    return bpm
