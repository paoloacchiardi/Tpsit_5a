import socket as sck

def client():

    host = "192.168.88.87"
    port = 6000
    c = sck.socket(sck.AF_INET,sck.SOCK_DGRAM)
    print("Enter a message, exit for close.")
    msg = input("Enter an input:\t")
    if msg != "exit":
        c.sendto(msg.encode(),(host,port))
    c.close()

if __name__ == "__main__":
    client()