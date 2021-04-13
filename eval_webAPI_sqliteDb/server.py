from flask import Flask, request, jsonify
import sqlite3 as sql

app = Flask(__name__)

@app.route('/getOperation', methods = ['GET'])
def operation():
    if request.method == "GET":
        id = request.args["id"]
        psw = request.args["psw"]
        if(validate(id,psw)):
            operation = searchOperation(id)
            if(operation == "Error"):
                return jsonify({"operation" : "Error"})
            else:
                return jsonify({"operation" : operation})
        else:
            return jsonify({"operation" : "Authentication error"})

@app.route('/sendResult', methods = ['GET'])
def result():
    if request.method == "GET":
        id = request.args["id"]
        psw = request.args["psw"]
        result = request.args["result"]
        if(validate(id,psw)):
            if(addResult(id,result) == "Error"):
                return jsonify({"message" : "0"})
            else:
                return jsonify({"message" : "1"})
        else:
            return jsonify({"message" : "Authentication error"})

def validate(id,psw):
    try:
        database = sql.connect('operazioni.db', 5.0, 0, None, False)
        cursore = database.cursor()
        cursore.execute(f"SELECT * FROM Clients WHERE clientID == \"{int(id)}\" AND psw == \"{psw}\"")
        if(len(cursore.fetchall()) != 0): #if return something
            return 1
        else:
            return 0
    except Exception as error:
        print(f"database error: {error}")
        return 0

def searchOperation(id):
    try:
        database = sql.connect('operazioni.db', 5.0, 0, None, False)
        cursore = database.cursor()
        cursore.execute(f"SELECT operation FROM Operations WHERE clientID == \"{int(id)}\" AND result IS NULL ORDER BY operationID LIMIT 1")
        operation = cursore.fetchone()[0]
        if(len(operation) != 0): #if return something
            return operation
        else:
            return "Error"
    except Exception as error:
        print(f"database error: {error}")
        return "Error"

def addResult(id,result):
    try:
        database = sql.connect('operazioni.db', 5.0, 0, None, False)
        cursore = database.cursor()
        cursore.execute(f"UPDATE Operations SET result = {result} WHERE operationID IN (SELECT min(operationID) FROM Operations WHERE clientID == '{id}' AND result IS NULL)")
        database.commit()
        return "Okay"
    except Exception as error:
        print(f"database error: {error}")
        return "Error"

def main():
    app.run(host="127.0.0.1",debug=True)

if __name__=="__main__":
    main()