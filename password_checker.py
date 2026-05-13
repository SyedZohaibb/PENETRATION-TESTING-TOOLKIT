import string
from colorama import Fore

def password_checker():

    print(Fore.CYAN + "\n--- PASSWORD STRENGTH CHECKER ---")

    password = input("Enter Password: ")

    score = 0

    if len(password) >= 8:
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(char in string.punctuation for char in password):
        score += 1

    print()

    if score <= 2:
        print(Fore.RED + "Weak Password")

    elif score == 3 or score == 4:
        print(Fore.YELLOW + "Medium Password")

    else:
        print(Fore.GREEN + "Strong Password")