import socket as sck

def main():
    host = "192.168.0.126"
    port = 7000
    host_invio = "192.168.0.134"
    server = sck.socket(sck.AF_INET,sck.SOCK_DGRAM)
    client = sck.socket(sck.AF_INET,sck.SOCK_DGRAM)
    server.bind((host,port))
    data,address = server.recvfrom(4096)
    print(f"From connected user: {data.decode()}")
    if not data or data.decode() == "exit":
        print("Close the connection.")
    else:
        client.sendto(data,(host_invio,port))
    server.close()
    client.close()

if __name__ == "__main__":
    main()