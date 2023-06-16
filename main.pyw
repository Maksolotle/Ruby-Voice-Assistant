import config
import stt
import pyttsx3
import datetime
import webbrowser
import random
import openai
import os 
import sys
import pyautogui as pg


from time import strftime
from fuzzywuzzy import fuzz


viber = r'C:\\Users\\Kalyns\\AppData\\Local\\Viber\\viber.exe'

engine = pyttsx3.init()

def speak(what):
    print( what )
    engine.say( what )
    engine.runAndWait()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

now = datetime.datetime.now()
hour = now.hour

# openai_api_key
openai.api_key = ваш апи ключ, необязатленьно

#response = openai.Completion.create( 
#model="text-davinci-003", 
#prompt=speech,
#temperature=0.5, 
#max_tokens=300, 
#top_p=1.0, 
#frequency_penalty=0.5, 
#presence_penalty=0.0 
#)


print(f"{config.VA_NAME} (v{config.VA_VER}) начал свою работу ...")

#Приветствие
if hour < 12:
    speak("Доброе утро, cэр")
elif hour < 18:
    speak("Добрый день сэр")
else:
    speak("Добрый вечер, cэр")


def va_respond(voice: str):
    print(voice)
    cmd = recognize_cmd(filter_cmd(voice))

    if cmd['cmd'] not in config.VA_CMD_LIST.keys():
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
    for c, v in config.VA_CMD_LIST.items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > rc['percent']:
                rc['cmd'] = c
                rc['percent'] = vrt

    return rc


def execute_cmd(cmd: str):
    if cmd == 'help':
        # help
        speak('Я умею: Рассказовать шутки, открывать программы, и многое другое')
    elif cmd == 'ctime':
        # current time
        speak(strftime("%H:%M"))

    elif cmd == 'joke':
        jokes = ['Как смеются программисты? ... ехе ехе ехе',
                 'Свинья подошла к розетке и сказала: что брат замуровали?',
                 'Программист это машина для преобразования кофе в код',
                 'Я бы пошутил про химию, но боюсь реакции не будет, cэр']

        speak(random.choice(jokes))

    elif cmd == 'open_browser':
        speak('Открываю')
        webbrowser.open('https://www.google.com')
    elif cmd == 'open_calk':
        speak('Открываю')
        os.system("start C:\windows\system32\calc.exe")
    elif cmd == 'open_cmd':
        speak('Открываю')
        os.system("start C:\windows\system32\cmd.exe")
    elif cmd == 'kak_dela':
        speak('хорошо, а у вас как дела?')
    elif cmd == 'hello':
        speak('К вашим услугам, сэр')
    elif cmd == 'lol':
        speak('Ха-ха-ха, лол')
    elif cmd == 'name':
        speak(f'Меня зовут Макс, мой разработчик Maksolotle, я написан на языке программирования Пайтон')
    elif cmd == "open_youtube":
        speak('есть')
        webbrowser.open('https://www.youtube.com/')
    elif cmd == 'open_translate':
        speak('Открываю переводчик')
        webbrowser.open('https://translate.google.com/')
    elif cmd == 'stupid':
        answers = ['Очень тонкое замечание, сэр',
                   'Успокойтесь, сэр',
                   'Допустим, сэр',
                   'Да, вы правы сэр']

        speak(random.choice(answers))

    elif cmd == 'good':
        speak('Рад за вас, сэр')
    elif cmd == 'bad':
        speak('Увы каждому бывает плохо, сэр')
    elif cmd == 'off':
        speak('До свидания, сэр')
        sys.exit()
    elif cmd == 'pon':
        speak('Рад что вы поняли, сэр')
    elif cmd == 'anti_joke':
        speak('Я понимаю что это несмешно для вас, надеюсь я вас не обидел')
    elif cmd == 'music':
        speak('Включаю музыку')
        webbrowser.open('https://www.youtube.com/live/jfKfPfyJRdk?feature=share')
    elif cmd == 'thanks':
        speak('Всегда, к вашим услугам, сэр')
    elif cmd == 'telegram':
        webbrowser.open('https://xn--80affa3aj0al.xn--80asehdb/')
        speak('Открываю')
    elif cmd == 'open_viber':
        os.system("start "+ viber)
        speak('есть')
    elif cmd == 'screen':
        pg.hotkey("winleft", "prtsc")
        speak('есть')
    elif cmd == 'like':
        pg.click(498, 661)
        pg.click(561, 700)
        speak("есть")
    elif cmd == 'maks':
        yes = ['Да, сэр',
                   'К вашим услугам, сэр',
                   'Чем могу быть полезен, сэр?']

        speak(random.choice(yes))
    elif cmd == 'gmail':
        webbrowser.open('https://mail.google.com/')
        speak("есть")
    elif cmd == 'google_disk':
        webbrowser.open('https://drive.google.com/')
        speak("есть")
    else:
        print("...")

# начать прослушивание команд
stt.va_listen(va_respond)
