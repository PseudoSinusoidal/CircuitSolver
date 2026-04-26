''' 
    Title: CircuitSolver CLI

    Made By: PseudoSinusoidal

    Started: 2025-08-09  (YYYY-MM-DD)???

    Edit Log:
        Floppy 2026-04-25: UI and CoLoRs Update!

'''
from C555 import Calc555 # 555 IC Timer Calculator
from OLaw import OLawBase # Ohm's Law Calculator
from RCalc import RCalc # Resistor Tools
from CalcUtilities import show_menu

# Module Dictionary
modules = {
    "1": Calc555,
    "2": OLawBase,
    "3": RCalc
}

# ANSI Colors
RED = "\x1b[31m"
GREEN = "\x1b[32m"
YELLOW = "\x1b[33m"
BLUE = "\x1b[34m"
PURPLE = "\x1b[35m"
CYAN = "\x1b[36m"
RESET = "\x1b[0m"

mm = rf"""
=============================================================
   ____ _                _ _   ____        _
  / ___(_)_ __ ___ _   _(_) |_/ ___|  ___ | |_   _____ _ __
 | |   | | '__/ __| | | | | __\___ \ / _ \| \ \ / / _ \ '__|
 | |___| | | | (__| |_| | | |_ ___) | (_) | |\ V /  __/ |
  \____|_|_|  \___|\__,_|_|\__|____/ \___/|_| \_/ \___|_|

=============================================================
      {GREEN}Developed by PseudoSinusoidal      {YELLOW}Version: 1.0.0{RESET}
-------------------------------------------------------------
 {PURPLE}Please Select from the following choices:{RESET}

 [1] {YELLOW}555 Timer IC{RESET}
 [2] {YELLOW}Ohm's Law{RESET}
 [3] {YELLOW}Resistor Utilities{RESET}

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
            print("[!] Invalid value. Please try again.")
        pass
except KeyboardInterrupt:
    print("[!] Exiting Program...")
