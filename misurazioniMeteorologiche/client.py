import requests as rq

urlFinale = "http://localhost:5000/caricaMisura"
stop = False
while(not stop):
    scelta = int(input("0 -> Invia misura, 1 -> Ferma comunicazione\n"))
    if(scelta == 0):
        valore = int(input("Immetti il valore della misurazione ->\t"))
        nomeGrandezza = input("Immetti il nome della grandezza ->\t")
        nomeStazione = input("Immetti il nome della stazione -> \t")
        tempo = input("Immetti data e ora nel formato seguente (es . 2020-06-21 12:32:48.066025) -> \t")
        params = {'grandezza' : nomeGrandezza}
        operation = rq.get(url = "http://localhost:5000/getIdGrandezza", params = params)
        esito = operation.json()['message'] #operazione
        if(esito != "ok"):
            print("Operazione fallita.")
        else:
            idGrandezza = operation.json()['id']
            params = {'nome' : nomeStazione}
            operation = rq.get(url = "http://localhost:5000/getIdStazione", params = params)
            esito = operation.json()['message'] #operazione
            if(esito != "ok"):
                print("Operazione fallita.")
            else:
                idStazione = operation.json()['id']
                params = {'valore' : valore, 'idGrandezza' : idGrandezza, 'idStazione' : idStazione, 'tempo' : tempo}
                operation = rq.get(url = urlFinale, params = params)
                esito = operation.json()['message'] #operazione
                if(esito != "ok"):
                    print("Operazione fallita.")
                else:
                    print("Misurazione inserita.")
    elif(scelta == 1):
        stop = True
    else:
        print("Scelta non valida.")