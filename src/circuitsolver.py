''' 
    Title: CircuitSolver CLI

    Made By: PseudoSinusoidal & Floppy

    Started: 2025-08-09  (YYYY-MM-DD)
'''

from modules.OLaw import * 
from modules.RCalc import * 
from modules.BJTFET import *
from modules.IntCirc import *
from modules.Utilities import *

# Module Dictionary
modules = {
    "1": OLawBase,
    "2": RCalc,
    "3": BJTFET,
    "4": IntCirc
}

mm = rf"""
============================================================={YELLOW}
                  ,/      ___ _             _ _
                ,'/      / __(_)_ _ __ _  _(_) |_
              ,' /      | (__| | '_/ _| || | |  _|
            ,'  /_____   \___|_|_| \__|\_,_|_|\__|
          .'____    ,'    ___      _
               /  ,'     / __| ___| |_ _____ _ _
              / ,'       \__ \/ _ \ \ V / -_) '_|
             /,'         |___/\___/_|\_/\___|_|
            /'
{RESET}=============================================================
      {GREEN}Developed by PseudoSinusoidal      {YELLOW}Version: SOURCE{RESET}
-------------------------------------------------------------
 {PURPLE}Please select from the following choices:{RESET}

 [1] {YELLOW}Ohm's Law{RESET}
 [2] {YELLOW}Resistor Utilities{RESET}
 [3] {YELLOW}BJT & MOSFET Utilities{RESET}
 [4] {YELLOW}Integrated Circuit Utilities{RESET}

 [CTRL+C] {RED}Exit{RESET}
-------------------------------------------------------------"""

show_menu(mm)
try:
    while True:
        ms = input(" > ")
        if ms in modules: # Find module number
            modules[ms]()
            show_menu(mm)  # Show the menu again after module execution
        else:
            print(invalid)
        pass
except KeyboardInterrupt:
    print(f"\n{RED}[!] Exiting Program...{RESET}")
