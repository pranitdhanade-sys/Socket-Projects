import socket
import struct

HOST = '127.0.0.1'
PORT = 8096

server = socket.socket()
server.bind((HOST, PORT))
server.listen()

print("[+] Binary Protocol Server")


conn,_ = server.accept()
while True:
    raw_len = conn.recv(4)
    if not raw_len:
        break
    msg_len = struct.unpack('!I', raw_len)[0]
    msg = conn.recv(msg_len).decode()
    print("Recieved",msg)

    conn.sendall(struct.pack("!I", len(msg)) + msg.encode())

conn.close()
server.close()