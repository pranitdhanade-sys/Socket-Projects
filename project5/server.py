import socket 
import threading

HOST = '127.0.0.1'
PORT = 8080

clients = []

def handle_client(conn,addr):
    print(f"[+]{addr} joined")
    while True:
        try:
            msg = conn.recv(1024)
            if not msg:
                break
            for c in clients:
                if c != conn:
                    c.sendall(msg)
        except:
            break 
    clients.remove(conn)
    conn.close()
    print(f"[-]{addr} left")


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen()

print("[+] Chat Server running")

while True:
    conn,addr = server.accept()
    clients.append(conn)
    threading.Thread(target=handle_client,args=(conn, addr), daemon=True)