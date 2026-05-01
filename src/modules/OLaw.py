# Ohm's Law Calculator Module
# By Pseudosinusoidal
import math
from modules.Utilities import *

def OLawBase():
    formulas = {
        "2": ("power", "W", ["V * I", "R * I^2", "V^2 / R"], {
            "1": lambda V, I: V * I, "2": lambda R, I: R * (I ** 2), "3": lambda V, R: (V ** 2) / R
        }),
        "3": ("voltage", "V", ["R * I", "P / I", "√P * R"], {
            "1": lambda R, I: R * I, "2": lambda P, I: P / I, "3": lambda P, R: math.sqrt(P) * R
        }),
        "4": ("current", "A", ["√P / R", "P / V", "V / R"], {
            "1": lambda P, R: math.sqrt(P) / R, "2": lambda P, V: P / V, "3": lambda V, R: V / R
        }),
        "5": ("resistance", "Ω", ["V / I", "V^2 / P", "P / I^2"], {
            "1": lambda V, I: V / I, "2": lambda V, P: (V ** 2) / P, "3": lambda P, I: P / (I ** 2)
        })
    }
    labels = {"V": "Voltage", "I": "Amperage", "R": "Resistance", "P": "Wattage"}
    mm = f"{PURPLE} [*] Ohm's Law Calculator{RESET}\n\n   [1] {YELLOW}Formula Sheet{RESET}\n   [2] {YELLOW}Find Power{RESET}\n   [3] {YELLOW}Find Voltage{RESET}\n   [4] {YELLOW}Find Current{RESET}\n   [5] {YELLOW}Find Resistance{RESET}\n\n [CTRL+C] {RED}Back{RESET}\n"
    
    show_menu(mm)
    try:
        while True:
            ms = input(" > ")
            
            if ms == "1":
                clear()
                print(f"{PURPLE} [*] Ohm's Law Formulas: {RESET}\n\n   [{RED}Power{RESET}]      V * I\n   [{RED}Power{RESET}]      R * I^2\n   [{RED}Power{RESET}]      V^2 / R\n   [{YELLOW}Voltage{RESET}]    R * I\n   [{YELLOW}Voltage{RESET}]    P / I\n   [{YELLOW}Voltage{RESET}]    √P * R\n   [{BLUE}Current{RESET}]    √P / R\n   [{BLUE}Current{RESET}]    P / V\n   [{BLUE}Current{RESET}]    V / R\n   [{GREEN}Resistance{RESET}] V / I\n   [{GREEN}Resistance{RESET}] V^2 / P\n   [{GREEN}Resistance{RESET}] P / I^2\n")
                input("\n [!] Press enter to return to main menu.")
                show_menu(mm)

            elif ms in formulas:
                clear()
                _, unit, forms, funcs = formulas[ms]
                while True:
                    prompt_str = f" [?] {PURPLE}Select Formula:{RESET}\n" + "\n".join([f"   [{i+1}] {YELLOW}{f}{RESET}" for i, f in enumerate(forms)]) + "\n\n > "
                    fs = input(prompt_str)
                    
                    if fs in funcs:
                        func = funcs[fs]
                        args = func.__code__.co_varnames[:2]
                        val1 = is_valid(f" [?] Enter {labels[args[0]]}: ", "float")
                        val2 = is_valid(f" [?] Enter {labels[args[1]]}: ", "float")

                        ans = func(val1, val2)
                        ans, sn = notation(ans)
                        
                        input(f"   [!] {GREEN}{ans} {sn}{unit}{RESET} \n\n[!] Press enter to continue.\n\n")
                        show_menu(mm)
                        break
                    else:
                        print(invalid)
            else:
                print(invalid)
    except KeyboardInterrupt:
        print(terminate)
