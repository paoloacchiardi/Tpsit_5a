import socket as sck

def main():
    host = "192.168.0.126"
    port = 7000
    host_invio = "192.168.0.134"
    server = sck.socket(sck.AF_INET,sck.SOCK_DGRAM)
    client = sck.socket(sck.AF_INET,sck.SOCK_DGRAM)
    server.bind((host,port))
    server.listen()
    conn,address = server.accept()
    data = conn.recv(4096)
    print(f"From connected user: {data.decode()}")
    client.connect((host_invio,port))
    client.sendto(data, (host_invio,port))
    conn.close()
    client.close()
    server.close()

if __name__ == "__main__":
    main()