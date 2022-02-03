import socket
import threading

def client_receive():
    while True:
        msg = client.recv(2048).decode(FORMAT)
        
        if (msg == "USERNAME"):
            client.send(username.encode(FORMAT))
        else:
            print(msg)

def send_msg():
    while True:
        msg = "{}: ".format(username) + input("")
        client.send(msg.encode(FORMAT))

if __name__ == "__main__":
    FORMAT = "utf-8"

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 8000))

    username = input("Enter a username: ")

    thread_receive = threading.Thread(target = client_receive)
    thread_receive.start()

    thread_send = threading.Thread(target = send_msg)
    thread_send.start()
    
