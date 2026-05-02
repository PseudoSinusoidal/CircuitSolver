# BJT & MOSFET Calculations Module
# By Pseudosinusoidal
from modules.Utilities import *

def BJTFET():
    formulas = {
        "BJTBase": {
            "baseA": lambda CEAmps, CGain: round(CEAmps / CGain, 4),
            "baseR": lambda BaseV, BEVDrop, BaseA: round((BaseV - BEVDrop) / BaseA, 4),
            "baseW": lambda BaseV, BaseA: round(BaseV * BaseA, 4)
        },
        "FETGate": {
            "GateR": lambda GateV, GateA: round(GateV / GateA, 4)
        }
    }

    mm = f"{PURPLE} [*] BJT & MOSFET Calculator{RESET}\n\n   [1] {YELLOW}BJT Base Resistor{RESET} \n   [2] {YELLOW}MOSFET Gate Series Resistor{RESET}\n\n [CTRL+C] {RED}Back{RESET}\n"
    show_menu(mm)
    
    try:
        while True:
            ms = input(" > ")
            
            if ms == "1":
                clear()
                CGain = is_valid("[!] Default Current Gain is 10.\n[?] Leave blank to use default, or enter Gain: ", "float", allow_blank=True)
                if CGain == "":
                    CGain = 10
                BEVDrop = is_valid("[!] Default Base-Emitter Voltage Drop is 0.7 V.\n[?] Leave blank to use default, or enter new value: ", "float", allow_blank=True)
                if BEVDrop == "":
                    BEVDrop = 0.7
                CEAmps = is_valid("[?] Enter Collector-Emitter Current in Amps: ", "float")
                BaseV = is_valid("[?] Enter voltage applied to Base: ", "float")
                while True:
                    BaseA = formulas["BJTBase"]["baseA"](CEAmps=CEAmps, CGain=CGain)
                    BaseR = formulas["BJTBase"]["baseR"](BaseV=BaseV, BEVDrop=BEVDrop, BaseA=BaseA)
                    BaseW = formulas["BJTBase"]["baseW"](BaseV=BaseV, BaseA=BaseA)
                    BaseA_, SN1 = notation(BaseA)
                    BaseR_, SN2 = notation(BaseR)
                    BaseW_, SN3 = notation(BaseW)

                    print(f"\n\n  [*] Forced Current Gain: {GREEN}{CGain}{RESET}")
                    print(f"  [*] Base-Emitter Voltage Drop: {GREEN}{BEVDrop} V{RESET}")
                    print(f"  [*] Collector-Emitter Current: {GREEN}{CEAmps} A{RESET}")
                    print(f"  [*] Base Voltage: {GREEN}{BaseV} V{RESET}")
                    print(f"  [*] Base Driving Current: {GREEN}{BaseA_} {SN1}A{RESET}")
                    print(f"  [*] Base Resistor: {GREEN}{BaseR_} {SN2}Ω, {BaseW_} {SN3}W{RESET}")

                    vdm = input("\n[!] Type 'CG' to change current gain, 'CEA' for Collector-Emitter Amperage, or 'volt' for base pin voltage. Press enter for main menu.\n > ")
                    if vdm == "CG":
                        CGain = is_valid("[?] Enter new Forced Current Gain: ", "float")
                    elif vdm == "CEA":
                        CEAmps = is_valid("[?] Enter Collector-Emitter Amperage: ", "float")
                    elif vdm == "volt":
                        BaseV = is_valid("[?] Enter Base Voltage: ", "float")
                    else:
                        show_menu(mm)
                        break
                    clear()

            if ms == "2":
                clear() # Add that it is typically 12-20mA per pin max
                GateV = is_valid("[?] Enter voltage applied to Gate: ", "float")
                GateA = is_valid("[!] If driving from a microcontroller, the maximum current per pin is typically 12-20mA.\n[?] Enter the maximum current available for Gate: ", "float")
                GateR = formulas["FETGate"]["GateR"](GateV=GateV, GateA=GateA)
                GateR, SN3 = notation(GateR)
                GateW = GateV * GateA
                GateA, SN2 = notation(GateA)
                GateW, SN4 = notation(GateW) 
                clear()
                print(f"\n\n  [*] Driving Voltage: {GREEN}{GateV} V{RESET}")
                print(f"  [*] Max Current: {GREEN}{GateA} {SN2}A{RESET}")
                print(f"  [*] Gate Series Resistor: {GREEN}{GateR} {SN3}Ω, {GateW} {SN4}W (Instaneous Current){RESET}")
                null = input("\n\n[!] Press enter to continue.")
                show_menu(mm)

            else:
                print(invalid)
    except KeyboardInterrupt:
        print(terminate)
