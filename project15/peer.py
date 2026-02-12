import socket
import threading

PORT = 9000

def listen():
    server = socket.socket()
    server.bind(('', PORT))
    server.listen()
    conn,_ = server.accept()
    while True:
        print("Peer:",conn.recv(1024).decode())

def connect(ip):
    client = socket.socket()
    client.connect((ip,PORT))
    while True:
        client.sendall(input("You:").encode())

threading.Thread(target=listen,daemon=True).start()
connect(input("Peer IP:"))
