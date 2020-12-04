import socket as sck
import config as cnf #library, G e N are here

def main():
    c = sck.socket(sck.AF_INET,sck.SOCK_STREAM)
    c.connect(('localhost',6000))
    while(True):
        a = int(input("Insert a value for a:\t"))
        if(a < cnf.N):
            break
        print(f"a must be < {cnf.N}")
    a_upper = (cnf.G^a) % cnf.N #calculate a_upper
    c.sendall(str(a_upper).encode()) #send a_upper
    b_upper = (c.recv(4096)).decode() #receive b_upper = (cnf.G ^ b) % cnf.N
    print(f"Number -> {(int(b_upper)^a) % cnf.N}") #print number = (b_upper ^ a) % cnf.N
    c.close()

if __name__ == "__main__":
    main()