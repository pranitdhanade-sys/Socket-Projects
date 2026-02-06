import  socket

HOST = '127.0.0.1'
PORT = 8080

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen()

print("Echo Server started")
conn, addr = server.accept()
print("Connected:",addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.sendall(data)

conn.close()
server.close()