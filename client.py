import socket
import threading
import sys

import random
import my_colors

from colorama import Fore

def client_receive():
    while True:
        try:
            msg = client.recv(2048).decode(FORMAT)
            
            if (msg == "USERNAME"):
                client.send(username.encode(FORMAT))
            else:
                print(msg)

        except:
            print("Erorr!")
            client.close()
            sys.exit()

def send_msg():
    while True:
        msg = f"{client_color}{username}{Fore.RESET}: {input('')}"
        client.send(msg.encode(FORMAT))

if __name__ == "__main__":
    FORMAT = "utf-8"

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 8000))

    username = input("Enter a username: ")

    client_color = random.choice(my_colors.colors_arr)

    thread_receive = threading.Thread(target = client_receive)
    thread_receive.start()

    thread_send = threading.Thread(target = send_msg)
    thread_send.start()
    
