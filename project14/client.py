import socket

HOST = '127.0.0.1'
PORT = 8092

client = socket.socket()
client.connect((HOST, PORT))

client.sendall(input("Username: ").encode())
token = client.recv(1024).decode()

print("Your token:", token)
client.close()
