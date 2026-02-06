import socket

HOST = '127.0.0.1'
PORT = 8080

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((HOST,PORT))

while True:
    msg = input("Send:")
    if msg == "exit":
        break
    client.sendall(msg.encode())
    print("Echo:",client.recv(1024).decode())

client.close()
