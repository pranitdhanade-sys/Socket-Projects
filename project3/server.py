import socket

HOST = '127.0.0.1'
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen()

print("Calculator Server running")

conn, addr = server.accept()
print("Connected:", addr)

while True:
    data = conn.recv(1024)
    if not data:
        break

    data = conn.recv(1024)
    expr = data.decode()



    if expr.lower() == "exit":
        break

    try:
        result = str(eval(expr))
    except Exception:
        result = "Invalid Expression"

    conn.sendall(result.encode())

conn.close()
server.close()
