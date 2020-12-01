import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('localhost',6000))
while(True):
    mex = input("Insert a message:\t")
    s.sendall(mex.encode()) 
    if(mex == "shutdown"):
        break
    data = s.recv(4096)
    print(data.decode()) 
s.close()