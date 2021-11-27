import os

from sys import platform as _platform

def clear_console():

    if _platform == "win32" or _platform == "win64":
        # Windows 32-bit or Windows 64-bit
        os.system('cls')
    elif _platform == "linux" or _platform == "linux2":
        # linux
        os.system('clear')
    elif _platform == "darwin":
        # MAC OS X
        os.system('clear')
    else:
        # Otherwise
        os.system('clear')
