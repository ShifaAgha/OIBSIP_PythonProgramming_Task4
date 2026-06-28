# Random Password Generator — OIBSIP Python Programming, Task 4

A simple command-line Random Password Generator built in Python. The program generates secure random passwords based on user-defined preferences, including password length and character types.

No external libraries are required—it uses Python's built-in `random` and `string` modules.

## Features

* Generate random passwords of any desired length
* Choose which character types to include:

  * Uppercase letters (`A-Z`)
  * Lowercase letters (`a-z`)
  * Numbers (`0-9`)
  * Special symbols (`!@#$%^&*`, etc.)
* Validates user input and handles invalid entries gracefully
* Ensures at least one character type is selected
* Allows users to generate multiple passwords in a single session

## How to Run

No installation required. Simply run:

```bash
python password_generator.py
```

## Example Output

```text
==================================================
   Random Password Generator - OIBSIP Task 4
==================================================

Enter password length: 12

Include uppercase letters? (y/n): y
Include lowercase letters? (y/n): y
Include numbers? (y/n): y
Include symbols? (y/n): y

==================================================
Generated Password:
X7@kL!9pQ2#m
==================================================

Generate another password? (y/n): y
```

## Project Structure

```text
ShifaAgha_Task4/
├── password_generator.py   # main program
└── README.md               # this file
```

## Key Concepts Used

* Randomization using the `random` module
* Character set handling with the `string` module
* User input validation
* Conditional statements (`if`, `elif`, `else`)
* Loops for repeated password generation
* Functions for modular and reusable code

## Author

**Shifa Agha**
OIBSIP Python Programming Internship

GitHub: https://github.com/ShifaAgha/OIBSIP
