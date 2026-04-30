# Resistor Calculator Module
# By Pseudosinusoidal
from CalcUtilities import *

Band_Colors = "0. Black\n1. Brown\n2. Red\n3. Orange\n4. Yellow\n5. Green\n6. Blue\n7. Violet\n8. Grey\n9. White"
Multipliers = "0. Black\n1. Brown\n2. Red\n3. Orange\n4. Yellow\n5. Green\n6. Blue\n7. Violet\n8. Grey\n9. White\n10. Gold\n11. Silver"
Tolerances = "0. Brown\n1. Red\n2. Green\n3. Blue\n4. Violet\n5. Grey\n6. Gold\n7. Silver"
PPM = "0. Brown\n1. Red\n2. Orange\n3. Yellow\n4. Blue\n5. Violet"

Tolerance_List = {
    "0": "1%",
    "1": "2%",
    "2": "0.5%",
    "3": "0.25%",
    "4": "0.1%",
    "5": "0.05%",
    "6": "5%",
    "7": "10%"
}

PPM_List = {
    "0": "100",
    "1": "50",
    "2": "15",
    "3": "25",
    "4": "10",
    "5": "5"
}

def RCalc():
    formulas = {
        "Voltage": {
            "dividera": lambda Mul, Vo, Load: round(Mul * (Vo / Load), 4),
            "tresistance": lambda Vi, Idiv: Vi / Idiv,
            "R2": lambda Vo, Vi, Rtot: (Vo / Vi) * Rtot,
            "R1": lambda Rtot, R2: Rtot - R2,
            "rdissipation": lambda Idiv, R: round((Idiv ** 2) * R, 4),
            "voltagedrop": lambda Vi, R2, Load, R1: round(Vi * (R2 / (R1 + R2)), 4) if Load == "" else round((Vi * (R2 * Load) / (R2 + Load)) / (R1 + (R2 * Load) / (R2 + Load)), 4),
            "dividerw": lambda Vi, Idiv: round(Vi * Idiv, 4)
        },
        "Current": {
            "v_drop": lambda Iload, Rload: Iload * Rload,
            "ishunt": lambda Iload, Mul: Iload * Mul,
            "itot": lambda Iload, Ishunt: Iload + Ishunt,
            "rshunt": lambda Vdrop, Ishunt: round(Vdrop / Ishunt, 4),
            "rtot": lambda Vdrop, It: round(Vdrop / It, 4)
        }
    }
    mm = f"{PURPLE} [*] Resistance Calculator{RESET}\n\n   [1] {YELLOW}Resistor Color Code Lookup{RESET} \n   [2] {YELLOW}Voltage Divider{RESET} \n   [3] {YELLOW}Current Divider{RESET}\n\n [CTRL+C] {RED}Back{RESET}\n"
    show_menu(mm)  # Show the menu at the start
    # Menu Loop
    try:
        while True:
            ms = input(" > ")

            if ms == "1":
                clear()
                while True:
                    band_count = input("[?] Is this a 4, 5, or 6 band resistor?\n > ")
                    if band_count in ("4", "5", "6"):
                        break
                    print(invalid)
                clear()
                print(Band_Colors)
                while True:
                    r1 = is_valid("[?] Enter the first color (0-9): ", "int")
                    if 0 <= r1 <= 9: break
                    print("[!] Out of range.")

                while True:
                    r2 = is_valid("[?] Enter the second color (0-9): ", "int")
                    if 0 <= r2 <= 9: break
                    print("[!] Out of range.")

                if band_count in ("5", "6"):
                    while True:
                        r5 = is_valid("[?] Enter the third color (0-9): ", "int")
                        if 0 <= r5 <= 9: break
                        print("[!] Out of range.")
                    base_ohms = (r1 * 100) + (r2 * 10) + r5
                else:
                    base_ohms = (r1 * 10) + r2

                clear()
                print(Multipliers)
                while True:
                    r3 = is_valid("[?] Enter the multiplier color (0-11): ", "int")
                    if 0 <= r3 <= 11: break
                    print("[!] Out of range.")
                clear()
                print(Tolerances)
                while True:
                    r4 = is_valid("[?] Enter the tolerance color (0-7): ", "int")
                    if 0 <= r4 <= 7:
                        try:
                            Tol = Tolerance_List[str(r4)]
                            break
                        except KeyError:
                            print(invalid)
                    else:
                        print("[!] Out of range.")
                clear()
                ppm = "N/A"
                if band_count == "6":
                    print(PPM)
                    while True:
                        r6 = is_valid("[?] Enter the sixth color (0-5): ", "int")
                        if 0 <= r6 <= 5:
                            try:
                                ppm = PPM_List[str(r6)]
                                clear()
                                break
                            except KeyError:
                                print(f"{RED}[!] PPM value is invalid. Please try again.{RESET}")
                        else:
                            print("[!] Out of range.")

                if r3 <= 9:
                    rtm = base_ohms * (10 ** r3)
                elif r3 == 10:
                    rtm = float(base_ohms) * 0.1
                elif r3 == 11:
                    rtm = float(base_ohms) * 0.01

                rtm, sn = notation(rtm)
                input(f"[!] Resistor Value Breakdown:\n\n Resistance: {GREEN}{rtm} {sn}Ω{RESET}\n Tolerance: {GREEN}{Tol}{RESET}\n Parts Per Million: {GREEN}{ppm}{RESET}\n\n[!] Press enter to proceed.")
                show_menu(mm)
            
            elif ms == "2": # Voltage Division
                clear()
                Vi = is_valid("\n[?] Enter input voltage: ", "float")
                Vo = is_valid("[?] Enter desired output voltage: ", "float")
                Load = is_valid("[?] Enter LOAD resistance (Ohms), leave blank if signal: ", "float", allow_blank=True)
                if Load == "":
                    Idiv = is_valid("[?] Enter desired divider current in Amperes: ", "float")
                else:
                    Mul = is_valid("[!] Lower multiplier means MORE resistance and LESS current in division circuit (Typically 10)\n[?] Enter multiplier: ", "float")
                while True:
                    if Load != "":
                        Idiv = formulas["Voltage"]["dividera"](Mul=Mul, Vo=Vo, Load=Load)
                    Rtot = formulas["Voltage"]["tresistance"](Vi=Vi, Idiv=Idiv)
                    R2 = formulas["Voltage"]["R2"](Vo=Vo, Vi=Vi, Rtot=Rtot)
                    PR2 = formulas["Voltage"]["rdissipation"](Idiv=Idiv, R=R2)
                    R1 = formulas["Voltage"]["R1"](Rtot=Rtot, R2=R2)
                    PR1 = formulas["Voltage"]["rdissipation"](Idiv=Idiv, R=R1)
                    Vo_Chk = formulas["Voltage"]["voltagedrop"](Vi=Vi, R2=R2, Load=Load, R1=R1)
                    Pdiv = formulas["Voltage"]["dividerw"](Vi=Vi, Idiv=Idiv)
                    Idiv_disp = round(Idiv, 4)
                    R1_disp = round(R1, 4)
                    R2_disp = round(R2, 4)
                    Idiv_disp_, SN1 = notation(Idiv_disp)
                    Pdiv_, SN2 = notation(Pdiv)
                    R1_disp_, SN3 = notation(R1_disp)
                    PR1_, SN4 = notation(PR1)
                    R2_disp_, SN5 = notation(R2_disp)
                    PR2_, SN6 = notation(PR2)
                    Vo_Chk_, SN7 = notation(Vo_Chk)
                    clear()
                    print(f"\n\n  [*] Divider total amperage: {GREEN}{Idiv_disp_} {SN1}A{RESET}\n  [*] Divider total wattage: {GREEN}{Pdiv_} {SN2}W{RESET}\n  [*] Resistor 1: {GREEN}{R1_disp_} {SN3}Ω, {PR1_} {SN4}W {RESET}\n  [*] Resistor 2: {GREEN}{R2_disp_} {SN5}Ω, {PR2_} {SN6}W{RESET}\n  [*] Voltage with load: {GREEN}{Vo_Chk_} {SN7}V{RESET}")
                    
                    vdm  = input("\n[!] Type 'mul'/'cur' to change multiplier/current, 'volt' to change voltages, or 'load' to change load. Press enter for main menu.\n > ")
                    if vdm in ("mul", "cur"):
                        if Load == "":
                            Idiv = is_valid("[?] Enter desired divider current (A): ", "float")
                        else:
                            Mul = is_valid("[?] Enter new multiplier: ", "float")
                    elif vdm == "volt":
                        Vi = is_valid("\n[?] Enter input voltage: ", "float")
                        Vo = is_valid("[?] Enter desired output voltage: ", "float")
                    elif vdm == "load":
                        Load = is_valid("[?] Enter LOAD resistance (Ohms): ", "float")
                        if Load == "" and 'Mul' in locals():
                            Idiv = is_valid("[?] Enter desired divider current (A): ", "float")
                        elif Load != "" and 'Mul' not in locals():
                            Mul = is_valid("[?] Enter multiplier: ", "float")
                    else:
                        show_menu(mm)
                        break
                    clear()
                
            elif ms == "3": # Current Division
                clear()
                Iload = is_valid("\n[?] Enter desired output load current (Amps): ", "float")
                Rload = is_valid("[?] Enter load resistance (Ohms): ", "float")
                Mul = is_valid("[?] Enter shunt current multiplier (e.g., 10 for 10x load current): ", "float")
                while True:
                    Vdrop = formulas["Current"]["v_drop"](Iload=Iload, Rload=Rload)
                    Ishunt = formulas["Current"]["ishunt"](Iload=Iload, Mul=Mul)
                    Itot = formulas["Current"]["itot"](Iload=Iload, Ishunt=Ishunt)
                    Rshunt = formulas["Current"]["rshunt"](Vdrop=Vdrop, Ishunt=Ishunt)
                    Rtot = formulas["Current"]["rtot"](Vdrop=Vdrop, It=Itot)
                    Pload = round(Vdrop * Iload, 4)
                    Pshunt = round(Vdrop * Ishunt, 4)
                    Vdrop_disp = round(Vdrop, 4)
                    Itot_disp = round(Itot, 4)
                    Itot_disp_, SN1 = notation(Itot_disp)
                    Rtot_, SN2 = notation(Rtot)
                    Vdrop_disp_, SN3 = notation(Vdrop_disp)
                    Rshunt_, SN4 = notation(Rshunt)
                    Pshunt_, SN5 = notation(Pshunt)
                    Pload_, SN6 = notation(Pload)
                    print(f"\n\n  [*] Total Source Amperage: {GREEN}{Itot_disp_} A{RESET}")
                    print(f"  [*] Total Equivalent Resistance: {GREEN}{Rtot_} Ω{RESET}")
                    print(f"  [*] Parallel Voltage (V_drop): {GREEN}{Vdrop_disp_} V{RESET}")
                    print(f"  [*] Shunt Resistor required: {GREEN}{Rshunt_} Ω, {Pshunt_} W{RESET}")
                    print(f"  [*] Load power dissipation: {GREEN}{Pload_} W{RESET}")

                    vdm = input("\n[!] Type 'mul' to change multiplier, 'load' for load resistance, or 'cur' for load current. Press enter for main menu.\n > ")
                    if vdm == "mul":
                        Mul = is_valid("[?] Enter new shunt multiplier: ", "float")
                    elif vdm == "load":
                        Rload = is_valid("[?] Enter load resistance (Ohms): ", "float")
                    elif vdm == "cur":
                        Iload = is_valid("[?] Enter desired load current (Amps): ", "float")
                    else:
                        show_menu(mm)
                        break
                    clear()
            else:
                print(invalid)
    except KeyboardInterrupt:
        print(terminate)
