import socket

HOST = '127.0.0.1'
PORT = 8080

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen()

print("[+]File Server listening")

conn, addr = server.accept()
print("[+]Connected",addr)

filename = conn.recv(1024).decode()
print("[+]Recieving file:",filename)

with open("received_"+filename,"wb") as f:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        f.write(data)

print("[+]File received successfully")

conn.close()
server.close()