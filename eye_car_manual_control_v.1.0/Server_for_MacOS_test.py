import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50010              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
    soc.bind((HOST, PORT))
    soc.listen(1)
    conn, addr = soc.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
