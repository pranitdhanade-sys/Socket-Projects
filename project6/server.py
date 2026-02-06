import socket

HOST = '127.0.0.1'
PORT = 8085

html = """
<html>
<head><title>Socket Server</title></head>
<body>
<h1>Hello from Python Socket Server</h1>
</body>
</html>
"""

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("[+] HTTP Server running")

while True:
    conn, addr = server.accept()
    request = conn.recv(1024).decode()

    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/html\r\n"
        f"Content-Length: {len(html)}\r\n"
        "\r\n"
        + html
    )

    conn.sendall(response.encode())
    conn.close()
