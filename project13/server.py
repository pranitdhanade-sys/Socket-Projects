import socket
import os

HOST = '127.0.0.1'
PORT = 8091

server = socket.socket()
server.bind((HOST, PORT))
server.listen()

print("[+] HTTP File Server running")

while True:
    conn, _ == server.accept()
    request = conn.recv(1024).decode()

    filename = "test.txt"

    
