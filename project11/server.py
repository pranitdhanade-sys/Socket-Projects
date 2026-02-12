import socket
import threading
import os
import time
from shared import *

HOST = "0.0.0.0"
PORT = 8089
FILE_ROOT = "./files"

os.makedirs(FILE_ROOT, exist_ok=True)

def handle_client(conn, addr):
    print(f"[+] Client connected: {addr}")

    try:
        request = recv_packet(conn)
        if not request:
            return

        if request["version"] != PROTOCOL_VERSION:
            send_packet(conn, {"status": "ERROR", "msg": "Protocol mismatch"})
            return

        filename = request["filename"]
        offset = request.get("offset", 0)

        filepath = safe_path(FILE_ROOT, filename)

        if not os.path.exists(filepath):
            send_packet(conn, {"status": "ERROR", "msg": "File not found"})
            return

        filesize = os.path.getsize(filepath)
        checksum = sha256_file(filepath)

        send_packet(conn, {
            "status": "OK",
            "filesize": filesize,
            "checksum": checksum
        })

        with open(filepath, "rb") as f:
            f.seek(offset)
            sent = offset

            while sent < filesize:
                data = f.read(CHUNK_SIZE)
                if not data:
                    break
                conn.sendall(data)
                sent += len(data)

        print(f"[✓] Sent {filename} to {addr}")

    except Exception as e:
        print(f"[!] Error {addr}: {e}")
    finally:
        conn.close()

def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()

    print(f"[+] Secure File Server listening on {PORT}")

    while True:
        conn, addr = s.accept()
        t = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
        t.start()

if __name__ == "__main__":
    start_server()
