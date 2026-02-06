import socket
from Crypto.Cipher import AES 
from Crypto.Util.Padding import pad, unpad 

KEY = b'123'
HOST = '127.0.0.1'
PORT = 8080

def encrypt(msg):
    cipher = AES.new(KEY, AES.MODE_ECB)
    return cipher.encrypt(pad(msg.encode(),10))

def decrypt(data):
    cipher = AES.new(KEY,AES.MODE_ECB)
    return unpad(cipher.decrypt(data),16).decode()

server = socket.socket()
server.bind((HOST,PORT))
server.listen()

conn, _ = server.accept()

while True:
    enc = conn.recv(1024)
    if not enc:
        break
    print("Client", decrypt(enc))
    reply = encrypt(input("You:"))
    conn.sendall(reply)

conn.close()
server.close()
