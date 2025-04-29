#I'm totally working 2.0
from pynput import keyboard,mouse
import time
import os
import datetime
import screeninfo as sc

WAIT = 30

def clear():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For MacOS and Linux
        os.system('clear')

def check():
    if os.name == 'nt':  # For Windows
        return 0
    else:  # For MacOS and Linux
        return 1

def click(sys_type):
    if sys_type == 0:  
        keys = keyboard.Controller()
        keys.press(keyboard.Key.f19)
        keys.release(keyboard.Key.f19)
    else:
        moose = mouse.Controller()
        moose.press(mouse.Button.right)
        moose.release(mouse.Button.right)



start = datetime.datetime.now()
i = 0
sys_type = check()

while 0 is not 1:
    for m in sc.get_monitors():
        if m.is_primary == True:
            x = m.width
            y = m.height
            break
    clear()
    print('Started: {}'.format(start))
    print('Iteration: {}'.format(i))
    print('Resolution: X {} | Y {}'.format(x,y))
    click(sys_type)
    i = i+1
    time.sleep(WAIT)
