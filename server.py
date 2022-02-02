import socket
import threading

def handle_client(client):
    while True:
        # Might need to account for max length of a message (if it's too big)
        message = client.recv(2048)
        print(message.decode(FORMAT))

def server_receive():
    while True:
        client, addr = server.accept()
        print("Accepted connection from {}".format(addr))

        client.send("Welcome to the chat!".encode(FORMAT))
        client_data = client.recv(2048).decode(FORMAT)
        print(client_data)

        thread = threading.Thread(target = handle_client, args = (client,))
        thread.start()
        
if __name__ == "__main__":
    HOST = "127.0.0.1"
    PORT = 8000

    FORMAT = "utf-8"

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print("Server is listening on . . .")
    server_receive()



    



        





