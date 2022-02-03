import socket
import threading
import sys

def sendTo_allClients(msg):
    for i in range(len(clients_arr)):
        clients_arr[i].send(msg)

def handle_client(client):
    while True:
        try:
            msg = client.recv(2048)
            
            decoded_msg = msg.decode(FORMAT)
            actual_msg = get_actual_msg(decoded_msg)

            if (actual_msg == "/quit"):
                disconnect(client)
                sys.exit()
                
            else:
                if (actual_msg == "/help"):
                    client.send(print_help_menu().encode(FORMAT))

                elif (actual_msg == "/users"):
                    client.send(print_current_users().encode(FORMAT))

                # elif (actual_msg[0:5] == "/kick"):
                #     kicked_username = actual_msg[6:]
                #     print('here:', kicked_username)
                #     kick_user(kicked_username)

                else:
                    sendTo_allClients(msg)
        except:
            disconnect(client)
            sys.exit()

# def kick_user(username):
#     for i in range(len(clients_arr)):
#         if (users_arr[i] == username):
#             clients_arr[i].send("You have been kicked by an admin!".encode(FORMAT))

#             clients_arr.remove(clients_arr[i])
#             clients_arr[i].close()
            
#             sendTo_allClients(f"{username} has been kicked by an admin!".encode(FORMAT))
#             users_arr.remove(username)
#             break

def disconnect(client):
    for i in range(len(clients_arr)):
        if (clients_arr[i] == client):
            username = users_arr[i]

            clients_arr.remove(client)
            client.close()

            sendTo_allClients(f"{username} has disconnected!".encode(FORMAT))
            print(f"{username} has left")
            users_arr.remove(username)            
            break

def get_actual_msg(msg):
    actual_msg = ""
    for i in range(len(msg)):
        if msg[i] == ':':
            actual_msg += msg[i+2:]
            break
    return actual_msg

def print_help_menu():
    return "\nList of commands: " \
        "\n- /quit" \
        "\n- /users" \
        "\n"

def print_current_users():
    current_users = "\nActive users:\n"
    for i in range(len(users_arr)):
        current_users += "-" + users_arr[i] + '\n'
    return current_users

def server_receive():
    while True:
        client, addr = server.accept()
        print("Accepted connection from {}".format(addr))
        
        client.send("USERNAME".encode(FORMAT))
        username = client.recv(2048).decode(FORMAT)
        
        clients_arr.append(client)
        users_arr.append(username)

        print(f"{username} has connected\n") 

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

    print("Server is listening. . .")
    server_receive()



    



        





