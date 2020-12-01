import threading
import socket as sck
class ClientThread (threading.Thread): #classe creata
    def __init__(self,connessione,ip): #costruttore, sempre d'obbligo il "self", "__" si chiama dunder
        self.ip_address = ip #self sarebbe il this in java
        
        self.conn = connessione
    def run(self): 
        #esegue il thread
        while(1):
            data = self.conn.recv(4096).decode()
            print(f"Dato ricevuto: {data}\nricevuto da: {self.ip_address}")
            if(data == "break"):
                break
            self.conn.sendall(data)

            
        
def main():
    threads = []
    ip = 'localhost'
    port = 6000
    s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    s.bind((ip,port))
    s.listen()
    while(1):
        conn,address = s.accept()
        threads.append(ClientThread(conn,address))
        threads[len(threads)-1].start()


if __name__ == "__main__":
    main()