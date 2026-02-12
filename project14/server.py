import socket
import uuid

HOST = '127.0.0.1'
PORT = 8092

tokens = {}

server = socket.socket()
server.bind((HOST, PORT))
server.listen()

conn, _ = server.accept()

username = conn.recv(1024).decode()

token = str(uuid.uuid4())
tokens[token] = username

conn.sendall(token.encode())

conn.close()
server.close()
