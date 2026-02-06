import socket

HOST = '127.0.0.1'
PORT = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST,PORT))

data = client.recv(1024)
print("recieved", data.decode())

client.close()