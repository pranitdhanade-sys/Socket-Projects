import socket
from Crypto.Cipher import AES 
from Crypto.Util.Padding import pad, unpad 

KEY = b'123'
HOST = '127.0.0.1'
PORT = 8080

def encrypt(msg):
    cipher = AES.new(KEY, AES.MODE_ECB)
    return cipher.encrypt(pad(msg.encode(),16))

def decrypt(data):
    cipher = AES.new(KEY, AES.MODE_ECB)
    return unpad(cipher.decrypt(data),16).decode()

client = socket.socket()
client.connect((HOST,PORT))

while True:
    msg = input("YOU:")
    client.sendall(encrypt(msg))
    print("server:",decrypt(client.recv(1024)))

client.close()