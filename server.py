import socket
import threading

def sendTo_allClients(msg):
    for i in range(len(clients_arr)):
        clients_arr[i].send(msg)

def handle_client(client):
    while True:
        try:
            # Might need to account for max length of a msg (if it's too big)
            msg = client.recv(2048)
            sendTo_allClients(msg)

        except:
            for i in range(len(clients_arr)):
                if (clients_arr[i] == client):
                    username = users_arr[i]

                    clients_arr.remove(client)
                    client.close()

                    sendTo_allClients(f"{username} has disconnected!".encode(FORMAT))
                    users_arr.remove(username)
                    
                    break

def server_receive():
    while True:
        client, addr = server.accept()
        print("Accepted connection from {}".format(addr))
        
        client.send("USERNAME".encode(FORMAT))
        username = client.recv(2048).decode(FORMAT)
        
        clients_arr.append(client)
        users_arr.append(username)

        print(f"{username} has been properly connected") 

        msg = f"{username} has entered the chat!".encode(FORMAT)
        sendTo_allClients(msg)

        thread = threading.Thread(target = handle_client, args = (client,))
        thread.start()
        
if __name__ == "__main__":
    HOST = "127.0.0.1"
    PORT = 8000

    FORMAT = "utf-8"
    
    clients_arr = []
    users_arr = []
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print("Server is listening on . . .")
    server_receive()



    



        





