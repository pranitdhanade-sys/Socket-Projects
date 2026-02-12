import socket

HOST = '127.0.0.1'
PORT = 8097

client = socket.socket()
client.connect((HOST, PORT))

while True:
    cmd = input("Enter command (UPLOAD/DOWNLOAD): ")
    if cmd.lower() == "exit":
        break
    client.sendall(cmd.encode())

    if cmd.startswith("UPLOAD"):
        filename = cmd.split()[1]
        with open(filename, "rb") as f:
            while True:
                data = f.read(1024)
                if not data:
                    break
                client.sendall(data)
        client.sendall(b"__END__")

    if cmd.startswith("DOWNLOAD"):
        filename = cmd.split()[1]
        with open("client_" + filename, "wb") as f:
            while True:
                data = client.recv(1024)
                if data.endswith(b"__END__"):
                    f.write(data[:-7])
                    break
                f.write(data)

    print(client.recv(1024).decode())

client.close()
