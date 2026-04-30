''' 
    Title: CircuitSolver CLI

    Made By: PseudoSinusoidal & Floppy

    Started: 2025-08-09  (YYYY-MM-DD)
'''

from C555 import *
from OLaw import * 
from RCalc import * 
from BJTFET import *
from IntCirc import *
from CalcUtilities import *

# Module Dictionary
modules = {
    "1": Calc555,
    "2": OLawBase,
    "3": RCalc,
    "4": BJTFET,
    "5": IntCirc
}

mm = rf"""
============================================================={YELLOW}                                                                                                                 
                              .                                        
                             ..                                       
                            ...                                           
                           ....                                           
                          .....                                           
                         ......                                           
                        .......                                              
                       ........                                                
                      ....................                                      
                     ....................                                       
                    ....................                                        
                   ....................                                          
                              ........                                           
                              .......                                             
                              ......                                              
                              .....                                               
                              ....                                                
                              ...                                                 
                              ..                                                  
                              .                                                                                                                                                                                                            
{RESET}=============================================================
      {GREEN}Developed by PseudoSinusoidal      {YELLOW}Version: Beta{RESET}
-------------------------------------------------------------
 {PURPLE}Please select from the following choices:{RESET}

 [1] {YELLOW}555 Timer IC{RESET}
 [2] {YELLOW}Ohm's Law{RESET}
 [3] {YELLOW}Resistor Utilities{RESET}
 [4] {YELLOW}BJT & MOSFET Utilities{RESET}
 [5] {YELLOW}Integrated Circuit Utilities{RESET}

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
    print("\n[!] Exiting Program...")
