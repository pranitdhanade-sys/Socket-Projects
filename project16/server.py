import socket
import threading

HOST = '127.0.0.1'
PORT = 8093

rooms = {}

def handle_client(conn):
    room = conn.recv(1024).decode()
    if room not in rooms:
        rooms[room] = []
    rooms[room].append(conn)
    conn.sendall(f"Joined room: {room}".encode())

    while True:
        try:
            msg = conn.recv(1024)
            if not msg:
                break
            for c in rooms[room]:
                if c!= conn:
                    c.sendall(msg)
        except:
            break

    rooms[room].remove(conn)
    conn.close()

server = socket.socket()
server.bind((HOST,PORT))
server.listen()
print("[+] Chat room Server running")

while True:
    conn, _ = server.accept()
    threading.Thread(target=handle_client, args=(conn,),daemon=True).start()
    