from flask import Flask,render_template,url_for    
from  flask_sqlalchemy import SQLAlchemy 

from flask_mysqldb import MySQL

import datetime

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "Gsunny@944"
app.config["MYSQL_DB"] = "hostelmng"


mysql = MySQL(app)
# MySQL configurations


@app.route("/",methods = ["POST","GET"])


def index():


    cur  = mysql.connection.cursor();
   
    cur.execute("select * from resident")
   
    data1  = cur.fetchall()
    
    cur.execute("show columns from resident")
    data  = cur.fetchall()
    
    return render_template('index.html',data = [data,data1])



@app.route("/caretaker",methods = ["POST","GET"])

def caretaker():
    cur  = mysql.connection.cursor();
   
    cur.execute("select * from caretaker")
   
    data1  = cur.fetchall()
    
    cur.execute("show columns from caretaker")
    data  = cur.fetchall()
    
    return render_template('caretaker.html',data = [data,data1])
    
    
@app.route("/hello")
def show_user():
    # Greet the user
    
    return f'Hello sunny     !'

if __name__ == "__main__" :
    app.run(debug = True)