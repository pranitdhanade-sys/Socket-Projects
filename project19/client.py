import socket
import struct

HOST = '127.0.0.1'
PORT = 8096

client = socket.socket()
client.connect((HOST, PORT))

while True:
    msg = input("Send: ")
    if msg == "exit":
        break
    client.sendall(struct.pack('!I', len(msg)) + msg.encode())
    raw_len = client.recv(4)
    resp_len = struct.unpack('!I',raw_len)[0]
    resp = client.recv(resp_len).decode()
    print("Server:", resp)

client.close()
