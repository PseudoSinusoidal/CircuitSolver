# A library for the calculator modules to call upon for quick, common and helpful functions.
import os
from time import sleep
import math

# ANSI Colors
RED = "\x1b[31m"
GREEN = "\x1b[32m"
YELLOW = "\x1b[33m"
BLUE = "\x1b[34m"
PURPLE = "\x1b[35m"
CYAN = "\x1b[36m"
RESET = "\x1b[0m"

invalid = f"{RED}[!] Invalid value. Try again.{RESET}"
terminate = f"\n{RED}[!] Terminating module..{RESET}"

def is_valid(prompt, mode):
    ii = input(prompt)
    while True:
        try:
            if mode == "float":
                ii = float(ii) 
                break
            elif mode == "int":
                ii = int(ii)
                break
        except (ValueError, TypeError):
            ii = input(f"{RED}[!] Invalid input. Try again.{RESET}\n > ")
    return ii

def show_menu(mm):
    sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(mm)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def notation(value: float) -> tuple[float, str]:
    if value == 0.0:
        return 0.0, ""
    prefixes = {
        12: 'T', 9: 'G', 6: 'M', 3: 'k',
        0: '',
        -3: 'm', -6: 'μ', -9: 'n', -12: 'p', -15: 'f'
    }
    exponent = int(math.floor(math.log10(abs(value)) / 3.0) * 3)
    exponent = max(min(exponent, 12), -15)
    scaled_value = value / (10 ** exponent)
    scaled_value = round(scaled_value, 10)
    return scaled_value, prefixes.get(exponent, "")