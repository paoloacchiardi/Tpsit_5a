import socket as sck
import my_turtle        
import turtle
import logging

def ricezione_percorso(client):
    #chiedo da dove parti e dove vuoi andare 
    dato = input("inserire partenza e arrivo (arrivo,partenza): ")


    #inzio il From to al server
    client.sendall(dato.encode())
    logging.debug(f" client : arrivo e partenza inviati :{dato}")          #poi stampo sul file di log quello che ho inviato 
    print(client.recv(4096).decode())    #ack      
    
                           
    logging.debug(" client : il server ha ricevuto l'arrivo e la partenza") #poi lo stampo sul file log
    risultato = client.recv(4096).decode()
    client.sendall("pippo".encode())

    return risultato






ip = 'localhost'    #indirizzo a cui collegarsi
porta=6300              #porta a cui puntare 

logging.basicConfig(filename='example.log', level=logging.DEBUG)

client = sck.socket(sck.AF_INET, sck.SOCK_STREAM) #creare l'oggetto socket con cui gestiremo la comunicazione


wn = turtle.Screen()
wn.bgcolor("lightgreen")
client.connect((ip,porta))   #il client si connette all'indirizzo che gli abbiamo dato (tuple)
print(f"mi sono connesso  Ip:{ip} e PORT: {porta}")
 



while(True):

    #1)chiedo al client cosa vuole inviare (Image or Path) o chiudere
    risposta = input("vuoi richiedere un percorso? (P) - 'close' per chiudere: ")
    

    #2)controllo attraverso un if quale risposta ha scielto l'operatore
    if(risposta == 'P'):
        wn.clear()
        wn.bgcolor("lightgreen")
        try:
            #richiesta e restituzione percorso
            risultato = ricezione_percorso(client)

            print(f"recv data: {risultato}")
            logging.debug(f"client : percorso ricevuto : {risultato}")
            
        except Exception as error:
            print(f"Failed transfert: {error}")
            break

        
        if(not risultato == "spiacente, non ci sono percorsi disponibili per le due destinazioni"): 
            try: 
               
                t = turtle.Turtle()          #crea l'oggetto turtle e lo assegna alla variabile t
                t.color("blue")              #rende l'icona del colore blue 
                t.pensize(3)          
                my_turtle.esegui_percorso(risultato,t) #eseguo la turtle                
                del t
            except Exception as error:
                print(f"error turtle,{error}")
        
        print(f"risultato : {risultato}") #stampo a video il risultato 
        
    #se la risposta è uguale a "close" chiude il programma 
    elif(risposta == 'close'):
        break
        
wn.bye()
del wn 
client.close() #chiude il socket appena ha finito di eseguire il codice sopra