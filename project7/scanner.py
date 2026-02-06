import socket

target = input("Enter target IP(e.g. 127.0.0.1):")
start_port = 1
end_port = 1024

print(f"\n[+]Scannong {target}...\n")

for port in range(start_port,end_port+1):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((target,port))
    if result == 0:
        print(f"[OPEN] Port {port}")
    s.close()