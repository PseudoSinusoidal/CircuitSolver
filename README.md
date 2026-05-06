# CircuitSolver

## Overview
CircuitSolver is an advanced terminal styled electrical calculator, which includes some of the most used and unused calculations and formulas
developed into a tiny package. Developed by PseudoSinusoidal & Floppy this calculator will become your best bud when it comes to needing a calculator!

Please take a look at the [previews](#previews) section if you'd like to know the layout of the program before install.

- Sections
  - [Previews](#previews)
  - [Modules](#modules)
  - [Future Modules](#future-modules)
  - [Next Updates](#next-updates)
  - [Install](#install)
    - [Windows](#windows)
    - [Linux](#linux)
    - [Advanced](#advanced)

CircuitSolver is still being developed and is a long way from done so updates may be infrequent and bugfixes are common.\
If you do find any bugs please report them and we'll get them fixed right away!\
Any suggestions are very welcome and will help out a lot in development!

### Previews
#### Main Menu
<img width="592" height="416" alt="Main-Menu-Preview" src="https://github.com/user-attachments/assets/cd51d1bf-1383-45f8-98c3-1b1fe65b1af7" />

### Modules
Now with scientific notations and colors!
- Ohm's Law
  - Voltage
  - Current
  - Resistance
  - Formula List
- Resistors
  - Color Code to Resistance (Up to 6 band)
  - Voltage Divider
  - Current Divider
- BJT and MOSFET
  - BJT Base Resistor
  - MOSFET Gate Series Resistor
- Various Integrated Circuits
  - PC817 (Finding the resistance value for the IR LED)
  - 555 Timer
    - Astable Mode
      - Frequency to Component
      - Component to Frequency
    - Monostable Mode
      - Duration to Components
      - Components to Duration

### Future Modules
- [ ]  Three Phase Real & Apparent Power
- [ ]  Root Mean Square Voltage
- [ ]  Kinematics

### Next Updates
- [ ]  Transformer Utilities (Turns ratio, waste power & efficiency)
- [ ]  LM317 Resistor Configuration
- [ ]  Stepper Motor Calibration
- [ ]  OP AMP Gain
- [ ]  Zener Diode Series Resistor under Load
- [ ]  Buck & Boost Converter

## Install
### Windows
To use CircuitSolver using a portable package (or executable and desktop shortcut), navigate to the [releases](https://github.com/PseudoSinusoidal/CircuitSolver/releases) page and download the latest version (or a previous version if needed) then, run the portable or executable file.

### Linux
(Requires: [pre-install dependencies](#pre-install-dependencies))
To use CircuitSolver using linux, run the below command for the latest version.
```
curl -fsSL https://raw.githubusercontent.com/PseudoSinusoidal/CircuitSolver/cli/install.sh | bash
```

### Advanced
(Requires: [pre-install dependencies](#pre-install-dependencies))
To use CircuitSolver using the SOURCE files, go to the [releases](https://github.com/PseudoSinusoidal/CircuitSolver/releases) page and download a zip from the version of your choosing.
Next unzip the file and using a terminal navigate into the src folder and run the below command.
```
python circuitsolver.py
```

### Pre-Install Dependencies
```
python 3
```
