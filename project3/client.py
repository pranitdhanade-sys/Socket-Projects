import socket

HOST = '127.0.0.1'
PORT = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

while True:
    expr = input("Enter Expression: ")

    if expr.lower() == "exit":
        client.sendall(expr.encode())
        break

    client.sendall(expr.encode())
    result = client.recv(1024).decode()
    print("Result:", result)

client.close()
