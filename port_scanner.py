import socket
from colorama import Fore

def port_scanner():
    print(Fore.CYAN + "\n--- PORT SCANNER ---")

    target = input("Enter IP Address: ")

    print(Fore.YELLOW + f"\nScanning {target}...\n")

    for port in range(20, 101):

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        result = sock.connect_ex((target, port))

        if result == 0:
            print(Fore.GREEN + f"Port {port} is OPEN")

        sock.close()