def main():
    alfabeto = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,
                     'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
    messaggio = "ciao"
    chiave = "itisdelpozzo"
    messaggio_cifrato = cifratura(messaggio,chiave,alfabeto)
    print(f"{messaggio_cifrato}")

def cifratura(parola,chiave,dizionario):
    vett = []
    for lettera in parola:
        vett.append(dizionario[lettera])
    key = []
    for lettera in chiave:
        key.append(dizionario[lettera])
    k=0
    for value in vett:
        vett[k] += key[k]
        vett[k] = vett[k] % len(dizionario)
        k += 1
    return vett

if __name__ == "__main__":
    main()