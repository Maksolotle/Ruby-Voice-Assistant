import os
import time

main = r'APP\main.py'
interface = r'GUI\Maks-Voice-Assistant\src-tauri\target\release\Maks-Voice-Assistant.exe'

os.system("start " + main)

time.sleep(5.2)

os.system("start " + interface)
