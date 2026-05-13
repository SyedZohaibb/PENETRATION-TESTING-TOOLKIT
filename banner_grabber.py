import socket
from colorama import Fore

def banner_grabber():

    print(Fore.CYAN + "\n--- BANNER GRABBER ---")

    host = input("Enter Website or IP: ")
    port = int(input("Enter Port: "))

    try:
        sock = socket.socket()
        sock.settimeout(2)

        sock.connect((host, port))

        sock.send(b"HELLO\r\n")

        banner = sock.recv(1024)

        print(Fore.GREEN + "\nBanner Information:")
        print(banner.decode())

        sock.close()

    except:
        print(Fore.RED + "Could not grab banner.")