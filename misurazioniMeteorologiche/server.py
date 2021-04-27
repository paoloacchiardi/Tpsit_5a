from flask import Flask, request, jsonify
import sqlite3 as sql

app = Flask(__name__)

@app.route('/getIdGrandezza', methods = ['GET'])
def getGrandezza():
    if request.method == "GET":
        if 'grandezza' in request.args:
            grandezza = request.args["grandezza"]
            idGrandezza = cercaIdGrandezza(grandezza)
            if(idGrandezza == "error"):
                return jsonify({"message" : "Grandezza non trovata."})
            elif(idGrandezza == "db error"):
                return jsonify({"message" : "Errore del db."})
            else:
                return jsonify({"message" : "ok",
                "id" : idGrandezza})
        else:
            return jsonify({"message" : "Incorrect params"})     

@app.route('/getIdStazione', methods = ['GET'])
def getStazione():
    if request.method == "GET":
        nome = request.args["nome"]
        if 'nome' in request.args:
            idStazione = cercaIdStazione(nome)
            if(idStazione == "error"):
                return jsonify({"message" : "Stazione non trovata."})
            elif(idStazione == "db error"):
                return jsonify({"message" : "Errore del db."})
            else:
                return jsonify({"message" : "ok",
                "id" : idStazione})
        else:
            return jsonify({"message" : "Incorrect params"})

@app.route('/caricaMisura', methods = ['POST','GET'])
def caricaMisurazione():
    if request.method == "GET":
        if ('valore' in request.args) and ('idGrandezza' in request.args) and ('idStazione' in request.args) and ('tempo' in request.args):
            valore = request.args["valore"]
            idGrandezza = request.args["idGrandezza"]
            idStazione = request.args["idStazione"]
            tempo = request.args["tempo"]
            if(caricaValore(valore,idGrandezza,idStazione,tempo)):
                return jsonify({"message" : "ok"})
            else:
                return jsonify({"message" : "error"})
        else:
            return jsonify({"message" : "Incorrect params"})

@app.route('/infoMisurazioni', methods = ['POST','GET'])
def info():
    if request.method == "GET":
        if ('idStazione' in request.args) and ('idGrandezza' in request.args):
            idGrandezza = request.args["idGrandezza"]
            idStazione = request.args["idStazione"]
            valori = getInfo(idGrandezza, idStazione)
            if(valori == "error"):
                return jsonify({"message" : "Valori non trovati."})
            elif(valori == "db error"):
                return jsonify({"message" : "Errore del db."})
            else:
                diz = valori.replace('(', '')
                diz1 = diz.replace(')', '')
                dizionario = diz1.split(',')
                return jsonify({"status" : "ok",
                    "massimo" : dizionario[0],
                    "minimo" : dizionario[1],
                    "media" : dizionario[2]
                })
        else:
            return jsonify({"message" : "Incorrect params"})

def getInfo(idGrandezza, idStazione):
    try:
        database = sql.connect('meteo_db.db', 5.0, 0, None, False)
        cursore = database.cursor()
        cursore.execute(f"SELECT max(valore) 'Massimo', min(valore) 'Minimo', avg(valore) 'Media' FROM misurazioni WHERE id_stazione == {idStazione} AND id_grandezza == {idGrandezza}")
        valori = str(cursore.fetchall()[0])
        if(len(valori) != 0): #if return something
            return valori
        else:
            return "error"
    except Exception as error:
        print(f"database error: {error}")
        return "db error"

def caricaValore(valore,idGrandezza,idStazione,tempo):
    try:
        database = sql.connect('meteo_db.db', 5.0, 0, None, False)
        cursore = database.cursor()
        cursore.execute(f"INSERT INTO misurazioni (id_stazione,id_grandezza,data_ora,valore) VALUES ({idStazione},{idGrandezza},'{tempo}',{valore})")
        database.commit()
        return 1
    except Exception as error:
        print(f"database error: {error}")
        return 0

def cercaIdGrandezza(grandezza):
    try:
        database = sql.connect('meteo_db.db', 5.0, 0, None, False)
        cursore = database.cursor()
        cursore.execute(f"SELECT id_misura FROM grandezze WHERE grandezza_misurata == '{grandezza}'")
        id = str(cursore.fetchone()[0])
        if(len(id) != 0): #if return something
            return id
        else:
            return "error"
    except Exception as error:
        print(f"database error: {error}")
        return "db error"

def cercaIdStazione(nome):
    try:
        database = sql.connect('meteo_db.db', 5.0, 0, None, False)
        cursore = database.cursor()
        cursore.execute(f"SELECT id_stazione FROM stazioni WHERE nome == '{nome}'")
        id = str(cursore.fetchone()[0])
        if(len(id) != 0): #if return something
            return id
        else:
            return "error"
    except Exception as error:
        print(f"database error: {error}")
        return "db error"

def main():
    app.run(host="127.0.0.1",debug=True)

if __name__=="__main__":
    main()