from modules.Utilities import *

def IntCirc():
    pass # WIP


# 555 Timer Calculator Module
# By Pseudosinusoidal
def Calc555():
    formulas = {
        "Monostable": {
            "duration": lambda Dur, C1: round((Dur / 1.1) / C1, 4), # Find R1 from Duration and C1
            "components": lambda R1, C1: round(1.1 * R1 * C1, 4) # Find Duration from R1 and C1
        },
        "Astable": {
            "TotalR": lambda Hz, C1: round((1.44 / Hz) / C1, 5), # Find total resistance from Hz and C1
            "ohmsper": lambda TotR: round(TotR / 3, 2), # Find R1 and R2 from Total Resistance
            "components": lambda R1, R2, C1: round(1.44 / (((R2 * 2) + R1) * C1), 5), # Find Hz from R1, R2, and C1.
            "highdur": lambda TotR, C1: round(0.693 * ((TotR / 3) * 2) * C1, 5), # Find High Time from Total Resistance and C1.
            "lowdur": lambda TotR, C1: round(0.693 * (TotR / 3) * C1, 5), # Find Low Time from Total Resistance and C1.
            "duty": lambda Th, Tl: round(Th / (Th + Tl) * 100, 5) # Find Duty Cycle from Time High and Time Low.
        }
    }

    mm = f"{PURPLE} [*] 555 Timer Calculator{RESET}\n\n   [1] {YELLOW}Monostable{RESET} \n   [2] {YELLOW}Astable{RESET}\n\n [CTRL+C] {RED}Back{RESET}\n"
    show_menu(mm) 
    
    try:
        while True:
            ms = input(" > ")

            # Monostable
            if ms == "1":
                clear()
                print(f" {PURPLE}[*] Monostable Formula T = 1.1 * R1 * C1{RESET}\n  {GREEN}Find by:{RESET}\n\n   [1] {YELLOW}Duration Required{RESET}\n   [2] {YELLOW}Component Values{RESET}\n")
                while True:
                    mono_menu = input(" > ")
                    if mono_menu == "1": # Finding Monostable Components from Required Duration
                        Dur = is_valid("[?] Enter Pulse Duration in Seconds: ", "float")
                        C1 = is_valid("[!] Default capacitor is 220uF. \n[?] Leave blank to use default, or enter in Farads: ", "float", allow_blank=True)
                        if C1 == "":
                            C1 = float(0.00022)
                        R1 = formulas["Monostable"]["duration"](Dur=Dur, C1=C1)
                        R1, SN = notation(R1)
                        Dur, SN2 = notation(Dur)
                        C1, SN3 = notation(C1)
                        null = input(f"[!] The required resistance to achieve {Dur} {SN2}s with {C1} {SN3}Farads is: \n\n   {GREEN}{R1}~ {SN}Ω{RESET}\n\n[!] Press enter to continue.")
                        show_menu(mm)
                        break

                    elif mono_menu == "2": # Finding Monostable Timing from Input Components
                        R1 = is_valid("[?] Resistor 1 Value in Ohms: ", "float")
                        C1 = is_valid("[?] Capacitor 1 Value in Farads: ", "float")
                        Time = formulas["Monostable"]["components"](R1=R1, C1=C1)
                        Time, SN = notation(Time)
                        null = input(f"[!] These components would produce a duration of: {GREEN}{Time}{RESET} {SN}s\n\n[!] Press enter to continue.")
                        show_menu(mm)
                        break

                    else:
                        print(invalid)
                
            # Astable
            elif ms == "2":
                clear()
                print(f" {PURPLE}[*] Astable Formula Hz = 1.44 / (R1 + 2*R2) * C1{RESET}\n  {GREEN}Find by:{RESET}\n\n   [1] {YELLOW}Frequency Required{RESET}\n   [2] {YELLOW}Component Values{RESET}\n")
                while True:
                    asta_menu = input(" > ")
                    if asta_menu == "1": # Finding Astable Components from Required Frequency
                        Hz = is_valid("[?] Enter the desired frequency in Hertz: ", "float")
                        C1 = is_valid("[?] Enter a preferred capacitance value in Farads: ", "float")
                        TotR = formulas["Astable"]["TotalR"](Hz=Hz, C1=C1)
                        ReqOhmsPer = formulas["Astable"]["ohmsper"](TotR=TotR)
                        Th = formulas["Astable"]["highdur"](TotR=TotR, C1=C1)
                        Tl = formulas["Astable"]["lowdur"](TotR=TotR, C1=C1)
                        DC = formulas["Astable"]["duty"](Th=Th, Tl=Tl)
                        Hz_, SN1 = notation(Hz)
                        C1_, SN2 = notation(C1)
                        ReqOhmsPer_, SN3 = notation(ReqOhmsPer)
                        TotR_, SN4 = notation(TotR)
                        Th_, SN5 = notation(Th)
                        Tl_, SN6 = notation(Tl)
                        if ReqOhmsPer < 1000:
                            print(f"{RED}[!] WARNING: Resistance Values under 1kΩ may damage 555 timer. Altering C1 value required.{RESET}")
                        null = input(f"[!] To achieve {Hz_} {SN1}Hz at {C1_} {SN2}Farads:\n\n [*] Resistance each: {GREEN}{ReqOhmsPer_} {SN3}Ω{RESET}\n [*] Time High: {GREEN}{Th_} {SN5}s{RESET}\n [*] Time Low: {GREEN}{Tl_} {SN6}s{RESET}\n [*] Duty Cycle: {GREEN}{DC} %{RESET}\n\n[!] Press enter to continue.\n[!] To change Resistance values and therefore Duty Rate, type 'editr' instead.\n\n > ")
                        
                        if null == "editr":
                            MaxR2 = (TotR / 2) - 1 # Finds and caps R2 value
                            print(f"\nThe total required value is {TotR_} {SN4}Ω which was by default achieved by {ReqOhmsPer_} {SN3}Ω per resistor.\nR2 must be 1.25 times R1 to achieve 50% Duty Rate. Time low cannot be higher than time high without a diode in parallel with R2.\n\n[CTRL+C] {RED}Exit{RESET}\n")
                            try:
                                while True:
                                    R2 = input(f"[?] Enter new R2 value [min: 1, max: {MaxR2}]: ")
                                    while True:
                                        try:
                                            R2 = float(R2)
                                            break
                                        except:
                                            print(invalid)
                                            R2 = input(" > ")
                                    if R2 > MaxR2 or R2 < 1:
                                        print("[!] Out of range")
                                    else:
                                        R1 = TotR - (R2 * 2) # Finding R1
                                        Th = round(0.693 * (R1 + R2) * C1, 5) # Finding High duration
                                        Tl = round(0.693 * R2 * C1, 5) # Finding Low duration
                                        DC = formulas["Astable"]["duty"](Th=Th, Tl=Tl)
                                        R1_, SN1 = notation(R1)
                                        R2_, SN2 = notation(R2)
                                        Th_, SN3 = notation(Th)
                                        Tl, SN4 = notation(Tl)
                                        print(f" [R1] {GREEN}{R1_} {SN1}Ω{RESET}\n [R2] {GREEN}{R2_} {SN2}Ω{RESET}\n [*] Time High: {GREEN}{Th_} {SN3}s{RESET}\n [*] Time Low: {GREEN}{Tl_} {SN4}s{RESET}\n [*] Duty Cycle: {GREEN}{DC} %{RESET}\n")
                            except KeyboardInterrupt:
                                print("\n[!] Returning..")
                            show_menu(mm)
                            break
                        else:
                            show_menu(mm)
                            break

                    elif asta_menu == "2": # Finding Astable Timing from Input Components
                        R1 = is_valid("[?] Resistor 1 Value in Ohms: ", "float")
                        R2 = is_valid("[?] Resistor 2 Value in Ohms: ", "float")
                        C1 = is_valid("[?] Capacitor Value in Farads: ", "float")
                        Hz = formulas["Astable"]["components"](R1=R1, R2=R2, C1=C1)
                        Th = round(0.693 * (R1 + R2) * C1, 5) # Finding High duration
                        Tl = round(0.693 * R2 * C1, 5) # Finding Low duration
                        DC = formulas["Astable"]["duty"](Th=Th, Tl=Tl)
                        Hz, SN1 = notation(Hz)
                        Th, SN2 = notation(Th)
                        Tl, SN3 = notation(Tl)
                        R1, SN4 = notation(R1)
                        R2, SN5 = notation(R2)
                        C1, SN6 = notation(C1)
                        null = input(f"\nUsing R1 {R1} {SN4}Ω, R2 {R2} {SN5}Ω and a capacitance of {C1} {SN6}Farads, you will achieve:\n [*] Frequency: {GREEN}{Hz} {SN1}Hz{RESET}\n [*] Time High: {GREEN}{Th} {SN2}s{RESET}\n [*] Time Low: {GREEN}{Tl} {SN3}s{RESET}\n [*] Duty Cycle: {GREEN}{DC} %{RESET}\n\n[!] Press enter to continue.")
                        show_menu(mm)
                        break

                    else:
                        print(invalid)
            else:
                print(invalid)
    except KeyboardInterrupt:
        print(terminate)
