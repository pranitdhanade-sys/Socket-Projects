import socket

HOST = '127.0.0.1'
PORT = 8080

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen(1)

print(f"[+]Server listening on {HOST}:{PORT}")

conn, addr = server.accept()
print(f"[+]Connected by {addr}")

conn.sendall(b"Hello World from Socket Server!")
conn.close()
server.close()