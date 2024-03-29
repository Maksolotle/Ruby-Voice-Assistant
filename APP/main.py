import config
import stt
import pyttsx3
import datetime
import webbrowser
import random
import os 
import sys
import pyautogui as pg
import subprocess
import yaml
import json
import time
import simpleaudio as sa

from time import strftime
from fuzzywuzzy import fuzz

def process_exists(process_name):
    while True:
        progs = str(subprocess.check_output('tasklist'))
        if process_name in progs:
            return True
        else:
            return False      


CDIR = os.getcwd()
VA_CMD_LIST = yaml.safe_load(
    open('commands.yaml', 'rt', encoding='utf8'),
)

# tts
# engine = pyttsx3.init()

def speak(what):
   print( what )
   engine.say( what )
   engine.runAndWait()



# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[2].id)

now = datetime.datetime.now()
hour = now.hour

name = config.user_name 

# play(f'{CDIR}\\sound\\ok{random.choice([1, 2, 3, 4])}.wav')
def play(phrase, wait_done=True):
    global recorder
    filename = f"{CDIR}\\sound\\"


    if phrase == "hello1":
        filename += "hello1.wav"
    elif phrase == "ok":
        filename += f"ok{random.choice([1, 2])}.wav"
    elif phrase == "joke":
        filename += f"joke{random.choice([1, 2, 3, 4])}.wav"
    elif phrase == "stupid":
        filename += f"stupid{random.choice([1, 2])}.wav"
    elif phrase == "hello2":
        filename += "hello2.wav"
    elif phrase == "hello3":
        filename += "hello3.wav" 
    elif phrase == "lol":
        filename += "lol.wav" 
    elif phrase == "pon":
        filename += "pon.wav" 
    elif phrase == "ready":
        filename += "ready.wav" 
    elif phrase == "story1":
        filename += "story1.wav" 
    elif phrase == "fine":
        filename += "fine.wav" 
    elif phrase == "good":
        filename += "good.wav" 
    elif phrase == "bad":
        filename += "bad.wav" 
    elif phrase == "name":
        filename += "name.wav" 
    elif phrase == "thanks":
        filename += "thanks.wav" 
    elif phrase == "close":
        filename += "close.wav"

    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()

print(f"{config.VA_NAME} (v{config.VA_VER}) начал свою работу ...")

#Приветствие
if hour < 12:
    play("hello1")
elif hour < 18:
    play("hello2")
else:
    play("hello3")


def va_respond(voice: str):
    print(voice)
    cmd = recognize_cmd(filter_cmd(voice))

    if cmd['cmd'] not in VA_CMD_LIST.keys():
        print("...")
    else:
        execute_cmd(cmd['cmd'])


def filter_cmd(raw_voice: str):
    cmd = raw_voice

    for x in config.VA_ALIAS:
        cmd = cmd.replace(x, "").strip()

    for x in config.VA_TBR:
        cmd = cmd.replace(x, "").strip()

    return cmd


def recognize_cmd(cmd: str):
    rc = {'cmd': '', 'percent': 70}
    for c, v in VA_CMD_LIST.items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > rc['percent']:
                rc['cmd'] = c
                rc['percent'] = vrt

    return rc






def execute_cmd(cmd: str):
    #if process_exists('Ruby-Voice-Assistant.exe'):
        #print()
    #else:
        #exit(0)
    
    # standard commands
    if cmd == 'help':
        play("help")
    elif cmd == 'ctime':
        speak(strftime("%H:%M")) # Here temporarily Pyttsx3
    elif cmd == 'ruby':
        play("ready")
    elif cmd == 'joke':
        play("joke")
    elif cmd == 'open_browser':
        play("ok")
        webbrowser.open('https://www.google.com')
    elif cmd == 'open_calk':
        play("ok")
        os.system("start C:\windows\system32\calc.exe")
    elif cmd == 'open_cmd':
        play("ok")
        os.system("start C:\windows\system32\cmd.exe")
    elif cmd == 'kak_dela':
        play("good")
    elif cmd == 'hello':
        play("ready")
    elif cmd == 'lol':
        play("lol")
    elif cmd == 'name':
        play("name")
    elif cmd == "open_youtube":
        play("ok")
        webbrowser.open('https://www.youtube.com/')
    elif cmd == 'open_translate':
         play("ok")
         webbrowser.open('https://translate.google.com/')
    elif cmd == 'stupid':
        play("stupid")
    elif cmd == 'good':
        play("fine")
    elif cmd == 'bad':
        play("bad")
    elif cmd == 'pon':
        play("pon")
    elif cmd == 'music':
        play("ok")
        webbrowser.open('https://music.youtube.com/')
    elif cmd == 'thanks':
        play("thanks")
    elif cmd == 'telegram':
        webbrowser.open('https://xn--80affa3aj0al.xn--80asehdb/')
        play("ok")
    elif cmd == 'screen':
        pg.hotkey("winleft", "prtsc")
        play("ok")
    elif cmd == 'open_telegram':
         # webbrowser.open('https://телеграм.онлайн/')
         subprocess.Popen([f'C:\\Users\\Kalyns\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe'])
         play("ok")
    elif cmd == 'close_browser':
        os.system("taskkill /im msedge.exe /f") # msedge.exe это браузер Microsoft Edge
        play("ok")
    elif cmd == 'role_up_windows':
        subprocess.Popen([f'{CDIR}\\ahk\\roll_up_windows.exe'])
        play("ok")
    elif cmd == 'empty_trash':
        subprocess.Popen([f'{CDIR}\\ahk\\empty_trash.exe'])
        play("ok")
    elif cmd == 'close':
        play("close")
        os.system("taskkill /im Maks-Voice-Assistant.exe /f")
        exit(0)
    elif cmd == 'block':
        play("ok")
        subprocess.Popen([f'{CDIR}\\ahk\\blocking.exe'])
    elif cmd == 'task_manager':
        pg.hotkey("ctrl", "shift", "esc")
        play("ok")
    elif cmd == 'lang':
        pg.hotkey("alt", "shift")
        play("ok")
    elif cmd == 'story':
        play("story1")
    elif cmd == 'mute_volume':
        subprocess.Popen([f'{CDIR}\\ahk\\mute_volume.exe'])
    elif cmd == 'close_calc':
        os.system("taskkill /im CalculatorApp.exe /f")
        play("ok")
    elif cmd == 'clipboard':
        subprocess.Popen([f'{CDIR}\\ahk\\clipboard.exe'])
        play("ok")
    elif cmd == 'sleep':
        subprocess.Popen([f'{CDIR}\\ahk\\sleep.exe'])

    elif cmd == 'full':
        pg.hotkey("f")
        play("ok")
    elif cmd == 'afull':
        pg.hotkey("esc")
        play("ok")
    elif cmd == 'pause':
        pg.hotkey("space")
        play("ok")
    elif cmd == 'c':
        pg.hotkey("c")
        play("ok")
    elif cmd == 'phonk':
        webbrowser.open('https://www.youtube.com/watch?v=0TF5QVs0tvM')
    elif cmd == 'md':
        webbrowser.open('https://www.mcdonalds.com/')
    elif cmd == 'dominos':
        webbrowser.open('https://dominos.ua/')

    elif cmd == 'powerpoint':
         subprocess.Popen([f'C:\\Program Files (x86)\\Microsoft Office\\Office16\\POWERPNT.exe'])
         play("ok")
    elif cmd == 'excel':
         subprocess.Popen([f'C:\\Program Files (x86)\\Microsoft Office\\Office16\\EXCEL.exe'])
         play("ok")
    elif cmd == 'word':
         subprocess.Popen([f'C:\\Program Files (x86)\\Microsoft Office\\Office16\\WINWORD.exe'])
         play("ok")

    elif cmd == 'gmail':
        webbrowser.open('https://mail.google.com/')
        play("ok") 
    elif cmd == 'maps':
        webbrowser.open('https://www.google.com/maps/')
        play("ok")
    elif cmd == 'drive':
        webbrowser.open('https://drive.google.com/')
        play("ok")
    # custom-commands
    elif cmd == 'viber':
        play("ok")
        subprocess.Popen([f'{CDIR}\\сustom-commands\\run_viber.exe'])
    

# начать прослушивание команд
stt.va_listen(va_respond)
