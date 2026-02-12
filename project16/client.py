import socket
import threading

HOST = "127.0.0.1"
PORT = 8093

def recieve_messages(sock):
    while True:
        try:
            print(sock.recv(1024).decode())
        except:
            break

client = socket.socket()
client.connect((HOST,PORT))


room  = input("Enter room name")
client.sendall(room.encode())

threading.Thread(target=recieve_messages, args=(client,), daemon=True).start()

while True:
    msg = input()
    if msg.lower() == "exit":
        break
    client.sendall(msg.encode)
client.close()