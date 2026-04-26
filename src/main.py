''' 
    Title: CircuitSolver CLI

    Made By: PseudoSinusoidal

    Started: 2025-08-09
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

mm = "[*] Electrical Calculators by Pseudosinusoidal\n[!] Enter the corresponding number to use module.\n[-1] Exit\n[1] 555 Timer IC\n[2] Ohm's Law\n[3] Resistor Calculator"

show_menu(mm)
while True:
    ms = input("> ")
    if ms == "-1":
        print("[!] Terminating program..")
        exit()
    elif ms in modules: # Find module number
        modules[ms]()
        show_menu(mm)  # Show the menu again after module execution
    else:
        print("[!] Invalid value. Try again.")
