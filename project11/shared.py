import os
import json
import hashlib
import struct

CHUNK_SIZE = 4096
PROTOCOL_VERSION = 1

def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(CHUNK_SIZE),b''):
            h.update(chunk)
        return h.hexdigest()
    
def send_packet(sock, data:dict):
    raw = json.dumps(data).encode()
    sock.sendall(struct.pack("!I", len(raw)))
    sock.sendall(raw)

def recv_packet(sock) -> dict:
    size_data = sock.recv(4)
    if not size_data:
        return None
    size = struct.unpack("!I",size_data)[0]
    raw = sock.recv(size)
    return json.loads(raw.decode())

def safe_path(base, filename):
    filename = os.path.basename(filename)
    return os.path.join(base, filename)
