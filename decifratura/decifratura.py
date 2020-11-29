def main():
    alfabeto = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,
                     'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
    messaggio = [10,1,8,6]
    chiave = "itisdelpozzo"
    messaggio_decifrato = decifratura(messaggio,chiave,alfabeto)
    print(f"{messaggio_decifrato}")

def decifratura(parola,chiave,dizionario):
    key_list = list(dizionario.keys())
    val_list = list(dizionario.values()) 
    k = 0
    chiave_vett = []
    for lettera in chiave:
        chiave_vett.append(dizionario[lettera])
    for num in parola:
        parola[k] -= chiave_vett[k]
        parola[k] = parola[k] % len(dizionario)
        k += 1
    vett = []
    index = 0
    for numero in parola:
        j = 0
        tro = False
        while(not tro):
            if(val_list[j] == numero):
                vett[index] = key_list[numero] #errore
                tro = True
            else:
                j += 1
        index += 1
    return vett

if __name__ == "__main__":
    main()