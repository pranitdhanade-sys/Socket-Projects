import socket
import os
import time
from shared import *

HOST = "127.0.0.1"
PORT = 8089

filename = input("Enter filename to download: ")
out_file = "downloaded_" + filename

offset = os.path.getsize(out_file) if os.path.exists(out_file) else 0

sock = socket.socket()
sock.connect((HOST, PORT))

send_packet(sock, {
    "version": PROTOCOL_VERSION,
    "filename": filename,
    "offset": offset
})

response = recv_packet(sock)

if response["status"] != "OK":
    print("[-]", response["msg"])
    sock.close()
    exit()

filesize = response["filesize"]
expected_hash = response["checksum"]

print(f"[+] File size: {filesize} bytes")
print(f"[+] Resuming at: {offset}")

received = offset
start = time.time()

with open(out_file, "ab") as f:
    while received < filesize:
        data = sock.recv(CHUNK_SIZE)
        if not data:
            break
        f.write(data)
        received += len(data)

        percent = (received / filesize) * 100
        print(f"\r[+] {percent:.2f}% downloaded", end="")

sock.close()

print("\n[+] Download finished")

actual_hash = sha256_file(out_file)

if actual_hash == expected_hash:
    print("[✓] Integrity verified (SHA-256)")
else:
    print("[!] File corrupted!")
