import requests as rq

url = "http://localhost:5000/getOperation"
stop = False
while(not stop):
    scelta = int(input("0 -> Termina processo, 1 -> Risolvi operazione\n"))
    if(scelta == 1):
        id = int(input("Immetti il tuo id ->\t"))
        psw = input("Immetti la password ->\t")
        params = {'id': id, 'psw': psw}
        operation = rq.get(url = url, params = params)
        data = operation.json()['operation'] #operazione
        if(data == "Error"):
            print("Operation not found.")
        elif(data == "Authentication error"):
            print("User not found.")
        else:
            print(f"Operazione -> {data}")
            result = eval(data)
            print(f"Risultato -> {result}")
            params = {'id': id, 'psw': psw, 'result': result}
            correct = rq.get(url = "http://localhost:5000/sendResult", params = params)
            response = correct.json()['message']
            if(response == "1"):
                print("Correct")
            elif(response == "0"):
                print("Error")
            else:
                print("Authentication error")
    elif(scelta == 0):
        stop = True
    else:
        print("Scelta non valida.")