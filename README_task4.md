# Random Password Generator — OIBSIP Python Programming, Task 4

A command-line password generator in Python. No external libraries needed —
runs on any machine with Python 3 installed.

## Features

- User specifies password length (4 – 128 characters)
- User chooses which character types to include:
  - Uppercase letters (A–Z)
  - Lowercase letters (a–z)
  - Numbers (0–9)
  - Symbols (!@#$%^&*...)
- Guarantees at least one character from each selected type
- Rates password strength: Weak / Moderate / Strong / Very Strong
- Handles invalid inputs (letters where numbers expected, length out of range, no type selected)
- Allows generating multiple passwords in one session

## How to Run

No installation needed. Just run:

```bash
python password_generator.py
```

## Example Output

```
==================================================
  Password Generator - OIBSIP Python Task 4
==================================================

Enter password length (4 - 128): 16

Select character types to include (enter yes or no):
  Include Uppercase letters (A-Z)? (yes/no): yes
  Include Lowercase letters (a-z)? (yes/no): yes
  Include Numbers (0-9)? (yes/no): yes
  Include Symbols (!@#$%^&*...)? (yes/no): yes

==================================================
        GENERATED PASSWORD
==================================================
  Password : aB3!xQ7#mK9@Lz2$
  Length   : 16
  Strength : Very Strong 💪
==================================================
```

## Key Concepts Used

- **Randomization** — `random.choice()` and `random.shuffle()` for secure, unpredictable passwords
- **Character Set Handling** — `string` module for letters/digits; custom symbols string
- **User Input Validation** — handles non-numeric input, out-of-range lengths, no type selected
- **Guaranteed Complexity** — mandatory characters ensure at least one of each selected type appears

## Project Structure

```
ShifaAgha_Task4/
├── password_generator.py   # main program
└── README.md               # this file
```

## Author

Shifa Agha — OIBSIP Python Programming Internship  
GitHub: https://github.com/ShifaAgha/OIBSIP
