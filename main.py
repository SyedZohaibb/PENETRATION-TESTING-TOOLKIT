from port_scanner import port_scanner
from password_checker import password_checker
from banner_grabber import banner_grabber
from ping_checker import ping_checker
from colorama import Fore, init

init(autoreset=True)

def menu():
    while True:
        print(Fore.CYAN + "\n===== PENETRATION TESTING TOOLKIT =====")
        print("1. Port Scanner")
        print("2. Password Strength Checker")
        print("3. Banner Grabber")
        print("4. Ping Checker")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            port_scanner()

        elif choice == "2":
            password_checker()

        elif choice == "3":
            banner_grabber()

        elif choice == "4":
            ping_checker()

        elif choice == "5":
            print(Fore.RED + "Exiting Toolkit...")
            break

        else:
            print(Fore.YELLOW + "Invalid Choice!")

menu()
