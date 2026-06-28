"""
Random Password Generator - OIBSIP Python Programming Task 4
-------------------------------------------------------------
Features:
    1. User specifies password length (min 4, max 128).
    2. User chooses character types:
         - Uppercase letters (A-Z)
         - Lowercase letters (a-z)
         - Numbers (0-9)
         - Symbols (!@#$%^&*...)
    3. Guarantees at least one character from each selected type.
    4. Generates multiple passwords in one session.
    5. Shows password strength rating (Weak / Moderate / Strong / Very Strong).
    6. Handles all invalid inputs gracefully.

Run:
    python password_generator.py
"""

import random
import string

# Character sets
UPPERCASE = string.ascii_uppercase       # A-Z
LOWERCASE = string.ascii_lowercase       # a-z
DIGITS    = string.digits                # 0-9
SYMBOLS   = "!@#$%^&*()_+-=[]{}|;:,.<>?"


def get_password_length():
    """Ask user for a valid password length between 4 and 128."""
    while True:
        try:
            length = int(input("Enter password length (4 - 128): "))
            if length < 4:
                print("  Minimum length is 4. Please try again.")
            elif length > 128:
                print("  Maximum length is 128. Please try again.")
            else:
                return length
        except ValueError:
            print("  Invalid input. Please enter a whole number.")


def get_character_choices():
    """Ask user which character types to include. At least one must be chosen."""
    print("\nSelect character types to include (enter yes or no):")
    choices = {}

    options = [
        ("uppercase", "Uppercase letters (A-Z)"),
        ("lowercase", "Lowercase letters (a-z)"),
        ("digits",    "Numbers (0-9)"),
        ("symbols",   "Symbols (!@#$%^&*...)"),
    ]

    for key, label in options:
        while True:
            ans = input(f"  Include {label}? (yes/no): ").strip().lower()
            if ans in ("yes", "y"):
                choices[key] = True
                break
            elif ans in ("no", "n"):
                choices[key] = False
                break
            else:
                print("  Please enter yes or no.")

    # At least one type must be selected
    if not any(choices.values()):
        print("  You must select at least one character type.")
        print("  Enabling all types by default.\n")
        return {k: True for k in choices}

    return choices


def build_character_pool(choices):
    """Build the full character pool and a list of mandatory characters."""
    pool = ""
    mandatory = []   # one char guaranteed from each selected type

    if choices.get("uppercase"):
        pool += UPPERCASE
        mandatory.append(random.choice(UPPERCASE))
    if choices.get("lowercase"):
        pool += LOWERCASE
        mandatory.append(random.choice(LOWERCASE))
    if choices.get("digits"):
        pool += DIGITS
        mandatory.append(random.choice(DIGITS))
    if choices.get("symbols"):
        pool += SYMBOLS
        mandatory.append(random.choice(SYMBOLS))

    return pool, mandatory


def generate_password(length, pool, mandatory):
    """
    Generate a password of the given length.
    Guarantees at least one character from each selected type
    by seeding the password with the mandatory characters,
    then filling the rest randomly, then shuffling.
    """
    remaining = length - len(mandatory)
    random_chars = [random.choice(pool) for _ in range(remaining)]
    password_list = mandatory + random_chars
    random.shuffle(password_list)
    return "".join(password_list)


def password_strength(length, choices):
    """Return a simple strength rating based on length and variety."""
    types_used = sum(choices.values())

    if length >= 16 and types_used == 4:
        return "Very Strong 💪"
    elif length >= 12 and types_used >= 3:
        return "Strong 👍"
    elif length >= 8 and types_used >= 2:
        return "Moderate ⚠️"
    else:
        return "Weak ❌"


def display_password(password, strength):
    """Print the generated password in a clear format."""
    print("\n" + "=" * 50)
    print("        GENERATED PASSWORD")
    print("=" * 50)
    print(f"  Password : {password}")
    print(f"  Length   : {len(password)}")
    print(f"  Strength : {strength}")
    print("=" * 50 + "\n")


def main():
    print("=" * 50)
    print("  Password Generator - OIBSIP Python Task 4")
    print("=" * 50 + "\n")

    while True:
        # Step 1: get length
        length = get_password_length()

        # Step 2: get character type choices
        choices = get_character_choices()

        # Step 3: build pool and generate
        pool, mandatory = build_character_pool(choices)
        password = generate_password(length, pool, mandatory)

        # Step 4: rate strength and display
        strength = password_strength(length, choices)
        display_password(password, strength)

        # Step 5: offer to generate another
        again = input("Generate another password? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("\nStay secure! Goodbye.")
            break
        print()


if __name__ == "__main__":
    main()
