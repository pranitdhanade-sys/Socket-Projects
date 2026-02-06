import socket

HOST = '127.0.0.1'
PORT = 8080

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((HOST,PORT))

client.sendall(input("Username:").encode())
client.sendall(input("Password:").encode())

print(client.recv(1024).decode())

client.close()
