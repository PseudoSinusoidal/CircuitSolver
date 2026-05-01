# BJT & MOSFET Calculations Module
# By Pseudosinusoidal
from modules.Utilities import *

def BJTFET():
    formulas = {
        "BJTBase": {
            "placeheld": lambda example: round(),
        },
        "FETGate": {
            "placeheld": lambda example: round()
        }
    }

    mm = f"{PURPLE} [*] BJT & MOSFET Calculator{RESET}\n\n   [1] {YELLOW}BJT Base Resistor{RESET} \n   [2] {YELLOW}MOSFET Gate Series Resistor{RESET}\n\n [CTRL+C] {RED}Back{RESET}\n"
    show_menu(mm)
    
    try:
        while True:
            ms = input(" > ")
            
            if ms == "1":
                clear()

            if ms == "2":
                clear()
                
            else:
                print(invalid)
    except KeyboardInterrupt:
        print(terminate)
