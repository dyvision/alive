# Import the required libraries
from tkinter import *
from pystray import MenuItem as item
import pystray
from PIL import Image, ImageTk
import os
from pynput.keyboard import Key, Controller
import time
import _thread

working_directory = 'C:\\Users\\{}\\AppData\\Roaming\\Alive'.format(
    os.getlogin())
keyboard = Controller()

# Create an instance of tkinter frame or window
win=Tk()
win.title("Alive")

# Define a function for quit the window
def quit_window(icon, item):
   icon.stop()
   win.destroy()

# Hide the window and show on the system taskbar
def hide_window():
   _thread.start_new_thread(online,())
   win.withdraw()
   image=Image.open("{}\\Alive.ico".format(working_directory))
   menu=(item('Quit', quit_window),)
   icon=pystray.Icon("name", image, "Alive", menu)
   icon.run()

win.protocol('WM_DELETE_WINDOW', hide_window)  

def online():
      while True:
         # Press and release space
         keyboard.press(Key.ctrl)
         keyboard.release(Key.ctrl)
         time.sleep(30)

win.command(hide_window())

win.mainloop()


