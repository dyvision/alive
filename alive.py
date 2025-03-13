#I'm totally working 2.0
from pynput.keyboard import Key, Controller
import time
import os
import datetime
import screeninfo as sc

def clear():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For MacOS and Linux
        os.system('clear')

start = datetime.datetime.now()
i = 0

while 0 is not 1:
    for m in sc.get_monitors():
        if m.is_primary == True:
            x = m.width
            y = m.height
            break
    clear()
    print('Started: {}'.format(start))
    print('Iteration: {}'.format(i))
    mouse = Controller()
    mouse.press(Key.f19)
    mouse.release(Key.f19)
    print('Resolution: X {} | Y {}'.format(x,y))
    mouse = ''
    i = i+1
    time.sleep(30)
