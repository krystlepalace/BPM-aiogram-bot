# BPM aiogram bot
 Telegram bot created with aiogram that can detect BPM from audiofile sent from user

[<img src="https://img.shields.io/badge/Telegram-%40bpm__detect__bot-blue">](https://t.me/bpm_detect_bot)
[![wakatime](https://wakatime.com/badge/user/4d0cc4aa-e1c1-483b-8c80-199c9ea5d0c5/project/7cb6b8ab-d040-4456-8eed-9d6d77b8a34e.svg)](https://wakatime.com/badge/user/4d0cc4aa-e1c1-483b-8c80-199c9ea5d0c5/project/7cb6b8ab-d040-4456-8eed-9d6d77b8a34e)

![Aiogram](https://img.shields.io/badge/aiogram-14354C?style=for-the-badge&logo=python&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

 # Contents
 1. <a href="#install">Install</a>
  * <a href="#prequisites">Prequisites</a> 
  * <a href="#basic-startup">Basic startup</a>
  * <a href="#systemd">Systemd</a>
 2. <a href="#todo">TODO</a>

## Install

### Prequisites
1. Python 3.11 or higher
2. Systemd (not done yet)

### Basic startup
Clone the repository and install all dependencies by:
```bash
pip install -r requirements.txt
```
Download ffmpeg or make sure you have it in PATH and fill .env variables.
If you are on Windows, insert full ffmpeg.exe path to .env variable. If you are on linux - just type 'ffmpeg'.

Fill other .env variables and start bot by:
```bash
python main.py
```

### Systemd
Work-in-progress

 ## TODO
1. User friendly interfice with inline buttons for redacting id3 tags
2. Systemd .service file 
