import socket as sck

def server():
    host = "192.168.88.74"
    port = 6200
    s = sck.socket(sck.AF_INET,sck.SOCK_DGRAM)
    s.bind((host,port))
    data,address = s.recvfrom(4096)
    print(f"From connected user: {data.decode()}")
    if not data or data.decode() == "exit":
        print("Close the connection.")
    s.close()

if __name__ == "__main__":
    server()