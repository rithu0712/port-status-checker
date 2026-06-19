import socket

host = input("Enter host (e.g., localhost or 127.0.0.1): ")
port = int(input("Enter port number: "))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(1)

result = sock.connect_ex((host, port))

if result == 0:
    print(f"Port {port} is OPEN")
else:
    print(f"Port {port} is CLOSED")

sock.close()
