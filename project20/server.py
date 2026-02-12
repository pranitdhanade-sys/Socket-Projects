import socket
import os

HOST = '127.0.0.1'
PORT = 8097

server = socket.socket()
server.bind((HOST, PORT))
server.listen()

print("[+] Mini FTP Server running")

conn, _ = server.accept()
while True:
    cmd = conn.recv(1024).decode()
    if not cmd:
        break

    parts = cmd.split()
    if parts[0] == "UPLOAD":
        filename = parts[1]
        with open("server_" + filename, "wb") as f:
            while True:
                data = conn.recv(1024)
                if data.endswith(b"__END__"):
                    f.write(data[:-7])
                    break
                f.write(data)
        conn.sendall(b"UPLOAD SUCCESS")
    elif parts[0] == "DOWNLOAD":
        filename = parts[1]
        if os.path.exists(filename):
            with open(filename, "rb") as f:
                while True:
                    data = f.read(1024)
                    if not data:
                        break
                    conn.sendall(data)
            conn.sendall(b"__END__")
        else:
            conn.sendall(b"ERROR")

conn.close()
server.close()
