from flask import Flask, jsonify, request
import sqlite3 as sql

app = Flask(__name__)

def checkParams(dizionario):
    if ('arrivo' in dizionario) and ('partenza' in dizionario):
        return True 
    else:
        return False

def percorsoDb(inizio,fine):

    try:
        database = sql.connect('percorsi.db', 5.0, 0, None, False)
        cursore = database.cursor()
    except Exception as error:
        print(f"database error: {error}")

    try :
        cursore.execute(f"SELECT percorso FROM percorsi INNER JOIN inizio_fine ON inizio_fine.id_percorso = percorsi.id WHERE (id_start = {inizio}) AND (id_end = {fine})")
        percorso = cursore.fetchone()
        print(percorso)
    except Exception as errordb:
        print(f"error database: {errordb}")
    
    if(len(percorso)==0):
        return "Path not found." 
    else:
        return percorso[0]

@app.route('/api/percorso', methods = ['GET'])
def api_percorso():
    if request.method == 'GET':
        if checkParams(request.args):
            arrivo = int(request.args['arrivo'])
            partenza = int(request.args['partenza'])
            percorso = percorsoDb(partenza,arrivo)
            if (percorso == "Path not found."):
                return "Path not found."
            else:
                return jsonify({"percorso" : percorso})
        else:
            return "Url not valid."

if __name__ == "__main__":
    app.run(host = '127.0.0.1' , debug = True)