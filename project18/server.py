import socket
import threading
import time

HOST = '127.0.0.1'
PORT = 8095

clients = {}
limit = 5  # messages per 10 seconds
interval = 10

def handle_client(conn):
    clients[conn] = []
    while True:
        try:
            msg = conn.recv(1024).decode()
            if not msg:
                break

            timestamps = clients[conn]
            now = time.time()
            timestamps = [t for t in timestamps if now - t < interval]
            if len(timestamps) >= limit:
                conn.sendall(b"Rate limit exceeded. Wait...")
                continue

            timestamps.append(now)
            clients[conn] = timestamps

            for c in clients:
                if c != conn:
                    c.sendall(msg.encode())

        except:
            break

    del clients[conn]
    conn.close()

server = socket.socket()
server.bind((HOST, PORT))
server.listen()
print("[+] Rate-Limited Chat Server")

while True:
    conn, _ = server.accept()
    threading.Thread(target=handle_client, args=(conn,), daemon=True).start()
