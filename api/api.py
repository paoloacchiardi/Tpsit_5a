from flask import Flask, request, jsonify
import sqlite3 as sql

app = Flask(__name__)

''' books = [
    { 'id': 0,
      'title' : 'Il nome della Rosa',
      'author' : 'Umberto Eco',
      'year_published' : '1980'
    },
    { 'id': 1,
      'title' : 'Il problema dei tre corpi',
      'author' : 'Liu Cixin',
      'year_published' : '2008'
    },
    { 'id': 2,
      'title' : 'Fondazione',
      'author' : 'Isaac Asimov',
      'year_published' : '1951'
    }
] '''

@app.route('/api/v1/resources/books',methods=['GET'])
def api_id(): #la richiesta get sarà localhost:5000/api/v1/resources/books
    if 'id' in request.args:
        id = int(request.args['id']) #if id is not in db, return null
    else:
        return "Error: no id provided. Specify an id."

    result = ricerca_id(id)
    
    return jsonify(result)

def ricerca_id(id):
    try:
        db = sql.connect('static/libreria_db.db',5.0,0,None,False)
        cursore = db.cursor()
        cursore.execute(f"SELECT * FROM Libri WHERE id == '{id}'")
    except Exception as error:
        print(f"Database error: {error}")
    result = cursore.fetchone()#[2]
    return result

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1')