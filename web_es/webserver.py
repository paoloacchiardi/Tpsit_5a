from flask import Flask, render_template, url_for, request, redirect #Render_template = import others html file, request = we can see in which mode website is called (post,get etc.)
import sqlite3 as sql                                                 #html name = request dictionary parameters, request.method, request.form['html name']
                                                                     #redirect('/rndpage') = going on another website, url_for('http://www') for website
app = Flask(__name__)
    
@app.route("/", methods=['GET','POST']) #http://127.0.0.1:5000/, di default Flask usa la porta 5000
def login():
    error = None
    if (request.method == 'POST'):
        for key,value in request.form.items():
            print(f"{key} -> {value}")
        username = request.form['name']
        password = request.form['psw']
        if(validate(username,password) == False):
            print("Error, values aren't in db.")
        else:
            return redirect('/pagina2')
    return render_template("login.html", error = error)

@app.route("/pagina2/") #http://127.0.0.1:5000/pagina2
def page():
    return "2nd page."

def validate(username,password):
        try:
            database = sql.connect('login_db.db', 5.0, 0, None, False)
            cursore = database.cursor()
        except Exception as error:
            print(f"database error: {error}")
            return 0
        cursore.execute(f"SELECT * FROM values_table WHERE username == \"{username}\" AND password == \"{password}\"")
        if len(cursore.fetchall()) != 0: #if return something
            return 1
        else:
            return 0

def main():
    app.run(host="127.0.0.1",debug=True)

if __name__=="__main__":
    main()