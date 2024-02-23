import socket
import threading

HOST = '127.0.0.1'
PORT = 1489
LIMIT = 10
active_clients = []

def listen_from_message(client, username):
    while True:
        message = client.recv(2048).decode('utf-8')
        if message:
            final_msg = username + '~' + message
            sending_message_to_all(final_msg)
        else:
            print(f"Message from {username} is empty")

def send_message_to_client(client, message):
    client.sendall(message.encode())

def sending_message_to_all(message):
    for user in active_clients:
        send_message_to_client(user[1], message)

def client_handler(client):
    while True:
        username = client.recv(2048).decode('utf-8')
        if username:
            active_clients.append((username, client))
            prompt_message = "CHATBOT ~" + f"{username} joined the chat"
            sending_message_to_all(prompt_message)
            break
        else:
            print("Username should not be empty")

    threading.Thread(target=listen_from_message, args=(client, username,)).start()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((HOST, PORT))
        print(f"Running the server on {HOST} {PORT}")
    except Exception as e:
        print(f"Unable to connect to Host {HOST} and port {PORT}")

    server.listen(LIMIT)
    while True:
        client, address = server.accept()
        print(f"Successfully connected to client {address[0]} {address[1]}")
        threading.Thread(target=client_handler, args=(client,)).start()

if __name__ == '__main__':
    main()
