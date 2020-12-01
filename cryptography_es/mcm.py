def Mcm(num_uno, num_due):
    tro = False
    if(num_uno == num_due):
        return num_uno
    elif(num_uno < num_due):
        magg = num_due
        minimo = num_uno
        while(not tro):
            if(minimo == magg):
                return magg
            elif(minimo < magg):
                minimo = minimo + num_uno
            else:
                magg = magg + num_due
    else:
        magg = num_uno
        minimo = num_due
        while(not tro):
            if(minimo == magg):
                return magg
            elif(minimo < magg):
                minimo = minimo + num_due
            else:
                magg = magg + num_uno
        

def main():
    num_uno = 0
    num_due = 0
    while(num_uno<=0 or num_due<=0):
        num_uno = int(input("Inserisci un 1o numero intero: "))
        num_due = int(input("Inserisci un 2o numero intero: "))
    print(f"Il minimo comune multiplo è: {Mcm(num_uno,num_due)}.")

if __name__ == "__main__":
    main()