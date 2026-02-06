import socket

HOST = '127.0.0.1'
PORT = 8086

users = {
    "admin" : "1234",
    "user" : "pass"
}

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("[+]Auth Server running")

conn, addr = server.accept()

username = conn.recv(1024).decode()
password = conn.recv(1024).decode()

if users.get(username) == password:
    conn.sendall(b"Login Success")
else:
    conn.sendall(b"LOGIN FAILED")

conn.close()
server.close()