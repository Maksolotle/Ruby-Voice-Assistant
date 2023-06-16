import os
import eel

main = r'C:\maksolotle\main.pyw'

os.system("start "+ main)


eel.init('web')
eel.start("main.html")