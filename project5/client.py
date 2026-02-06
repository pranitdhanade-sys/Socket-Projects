import socket
import threading

HOST = '127.0.0.1'
PORT = 8080

def recieve():
    while True:
        try:
            msg = client.recv(1024)
            print(msg.decode())
        except:
            break

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((HOST,PORT))

threading.Thread(target=recieve,daemon=True).start()

while True:
    msg = input()
    if msg == "exit":
        break
    client.sendall(msg.encode())

client.close()
