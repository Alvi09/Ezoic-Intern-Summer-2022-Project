import socket
import threading
import sys
import random
from colorama import Fore

import json
import time

import my_colors

def client_receive():
    while True:
        try:
            msg = client.recv(2048).decode(FORMAT)
            if (msg == "USERNAME"):
                client.send(username.encode(FORMAT))
            else:
                parsed_json = json.loads(msg)

                if (parsed_json['type'] == "server"):
                    print(f"{parsed_json['username']} {parsed_json['input']}")

                else:
                    color = parsed_json['color']
                    actual_username = parsed_json['username']
                    color_reset = parsed_json['color_reset']
                    user_input = parsed_json['input']
                    current_time = parsed_json['time']

                    actual_msg = f"[{current_time}] {color} {actual_username}: {color_reset} {user_input}"
                    print(actual_msg)

        except:
            print("Erorr!")
            client.close()
            sys.exit()

def send_msg():
    while True:
        user_input = input('')

        currentTime = time.strftime("%H:%M:%S")

        payload['input'] = user_input
        payload['type'] = "client"
        payload['time'] = str(currentTime)

        payload_json = json.dumps(payload)
        msg = payload_json

        client.send(msg.encode(FORMAT))




        # actual_msg = get_actual_msg(msg)
        # if (username == "ADMIN" and actual_msg[0:5] == "/kick"):            
        #         client.send(f"/kick {actual_msg[6:]}".encode(FORMAT))
        # else:

        # client.send(msg.encode(FORMAT))

def get_valid_username():
    username = ""
    while True:
        username = input("Enter a username: ")
        if (len(username) == 0):
            print("Usernames can't be empty! Try again\n")
        else:
            break
    return username

if __name__ == "__main__":
    FORMAT = "utf-8"

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 8000))

    username = get_valid_username()
    client_color = random.choice(my_colors.colors_arr)

    payload = {'color': client_color,
               'username': username,
               'color_reset' : Fore.RESET,
               'input': "",
               'type': "",
               'time': ""
    }


    thread_receive = threading.Thread(target = client_receive)
    thread_receive.start()

    thread_send = threading.Thread(target = send_msg)
    thread_send.start()

