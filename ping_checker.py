import os
from colorama import Fore

def ping_checker():

    print(Fore.CYAN + "\n--- PING CHECKER ---")

    host = input("Enter IP or Website: ")

    response = os.system(f"ping -n 1 {host}")

    if response == 0:
        print(Fore.GREEN + "\nHost is ACTIVE")

    else:
        print(Fore.RED + "\nHost is OFFLINE")