import socket as sck
import config as cnf #library, G e N are here

def main():
    while(True):
        b = int(input("Insert a value for b:\t")) 
        if(b < cnf.N):
            break
        print(f"b must be < {cnf.N}")
    s = sck.socket(sck.AF_INET,sck.SOCK_STREAM)
    s.bind(('localhost',6000))
    s.listen()
    conn,_ = s.accept()
    a_upper = (conn.recv(4096)).decode() #receive a_upper = (cnf.G ^ a) % cnf.N
    b_upper = (cnf.G^b) % cnf.N #calculate b_upper
    conn.sendall(str(b_upper).encode()) #send b_upper
    print(f"Number -> {(int(a_upper)^b) % cnf.N}") #print number = (a_upper ^ b) % cnf.N
    s.close()
    conn.close()

if __name__ == "__main__":
    main()