from ast import arguments
from shutil import copyfile
import os
import sys



locate_python = sys.exec_prefix

os.system('{}\\python -m pip install -r requirements.txt'.format(locate_python))
os.system('{}\\python -m pipwin install pywin32'.format(locate_python))
os.system('{}\\python -m pip install -U pystray --no-cache-dir'.format(locate_python))

from win32com.client import Dispatch

working_directory = 'C:\\Users\\{}\\AppData\\Roaming\\Alive'.format(
    os.getlogin())
start_directory = 'C:\\Users\\{}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\'.format(
    os.getlogin())
tray_file = 'tray.py'

# Create Folders
try:
    os.mkdir(working_directory)
except:
    pass
try:
    tray_path = "{}\\{}".format(working_directory, tray_file)
    icon_path = "{}\\Alive.ico".format(working_directory)
    copyfile(tray_file, tray_path)
    copyfile('Alive.ico', icon_path)
except:
    pass


path = os.path.join(start_directory, 'Alive.lnk')
target = "{}\\pythonw".format(locate_python) 
t_arguments = tray_path
icon = icon_path

shell = Dispatch('WScript.Shell')
shortcut = shell.CreateShortCut(path)
shortcut.TargetPath = target
shortcut.Arguments = t_arguments
shortcut.IconLocation = icon
shortcut.save()