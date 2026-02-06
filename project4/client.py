import socket
import os

HOST = '127.0.0.1'
PORT = 8080

filepath = input("Enter file path: ")
filename = os.path.basename(filepath)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

client.sendall(filename.encode())

with open(filepath, "rb") as f:
    while True:
        data = f.read(1024)
        if not data:
            break
        client.sendall(data)

client.close()
print("[+] File sent successfully")
