import socket
import threading
import os

HOST = '127.0.0.1'
PORT = 8094

rooms = {}  # room_name -> list of clients

def handle_client(conn):
    room = conn.recv(1024).decode()
    if room not in rooms:
        rooms[room] = []
    rooms[room].append(conn)

    # Send previous messages
    history_file = f"{room}.txt"
    if os.path.exists(history_file):
        with open(history_file, "r") as f:
            for line in f:
                conn.sendall(line.encode())

    while True:
        try:
            msg = conn.recv(1024)
            if not msg:
                break
            msg_text = msg.decode()
            with open(history_file, "a") as f:
                f.write(msg_text + "\n")
            for c in rooms[room]:
                if c != conn:
                    c.sendall(msg)
        except:
            break

    rooms[room].remove(conn)
    conn.close()

server = socket.socket()
server.bind((HOST, PORT))
server.listen()
print("[+] Persistent Chat Server running")

while True:
    conn, _ = server.accept()
    threading.Thread(target=handle_client, args=(conn,), daemon=True).start()
