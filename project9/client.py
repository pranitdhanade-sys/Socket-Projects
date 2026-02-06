import socket
import json

HOST = '127.0.0.1'
PORT = 8087

payload = {
    "action": "add",
    "a": 10,
    "b": 20
}

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
client.sendall(json.dumps(payload).encode())

response = json.loads(client.recv(1024).decode())
print("Result:", response["result"])

client.close()
