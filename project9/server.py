import socket
import json

HOST = '127.0.0.1'
PORT = 8087

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()


conn, addr = server.accept()
data = json.loads(conn.recv(1024).decode())

if data["action"] == "add":
    result = data['a'] + data['b']
else:
    result = "Unknown action"

response = json.dumps({"result":result})
conn.sendall(response.encode())

conn.close()
server.close()