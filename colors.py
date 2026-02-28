# colors.py
from colorama import Fore, Style, init
init(autoreset=True)

def black():
    return Fore.BLACK

def red():
    return Fore.RED

def green():
    return Fore.GREEN

def yellow():
    return Fore.YELLOW

def blue():
    return Fore.BLUE

def magenta():
    return Fore.MAGENTA

def cyan():
    return Fore.CYAN

def white():
    return Fore.WHITE

def light_black():
    return Fore.LIGHTBLACK_EX

def light_red():
    return Fore.LIGHTRED_EX

def light_green():
    return Fore.LIGHTGREEN_EX

def light_yellow():
    return Fore.LIGHTYELLOW_EX

def light_blue():
    return Fore.LIGHTBLUE_EX

def light_magenta():
    return Fore.LIGHTMAGENTA_EX

def light_cyan():
    return Fore.LIGHTCYAN_EX

def light_white():
    return Fore.LIGHTWHITE_EX

# Optional: functions for styles
def bright():
    return Style.BRIGHT

def dim():
    return Style.DIM

def normal():
    return Style.NORMAL
