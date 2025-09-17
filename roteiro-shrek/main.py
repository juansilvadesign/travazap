import pyautogui as pag
from time import sleep
sleep(2)
with open('shrek.txt','r') as shrek:
    for i in shrek.readlines():
        pag.write(i)
        pag.press('enter')