from flask import Flask                             # import Flask
from flask import render_template, request                   # render for templates & request to bring data from the user
from flaskext.mysql import MySQL                    # connect to database

app = Flask(__name__)                               # create the application
mysql = MySQL()                                     # connecting to the database
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='1234'
app.config['MYSQL_DATABASE_BD']='sistema'
mysql.init_app(app)                                 # create the connection 

@app.route("/")                                     # routing so that user enters root
def index():
    sql="INSERT INTO `sistema`.`pacientes` (`id`, `nombre`, `correo`, `foto`) VALUES (NULL, 'Juan Pablo', 'juanpablo@gmail.com', 'juanpablo.jpg');"
    conn=mysql.connect()                            # connect to mysql.init_app(app)
    cursor=conn.cursor()                            # store what runs
    cursor.execute(sql)                             # run the SQL statement
    conn.commit()                                   # close the connection
    return render_template("pacientes/index.html")  # identify the folder and the html file

@app.route('/create') 
def create(): 
    return render_template('pacientes/create.html')

@app.route("/store", methods=["POST"])
def storage():
    _nombre=request.form['txtNombre'] 
    _correo=request.form['txtCorreo'] 
    _foto=request.form['txtFoto']
    sql = "INSERT INTO `sistema`.`pacientes` (`id`, `nombre`, `correo`, `foto`) VALUES (NULL, %s, %s, %s);" 
    datos=(_nombre,_correo,_foto)
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, datos)                      # join the sql and datos variables 
    conn.commit()
    return render_template("pacientes/index.html")

if __name__=="__main__":                             
    app.run(debug=True)                             # set debug mode

#mysql=MySQL()
#app.config["MYSQL_DATABASE_HOST"]="localhost"
#app.config["MYSQL_DATABASE_USER"]="root"
#app.config["MYSQL_DATABASE_PASSWORD"]=""
#app.config["MYSQL_DATABASE_DB"]="localhost"
#mysql.init_app(app)

# @app.route("/")
#def index():
#    sql="INSERT INTO"
#    conn=mysql.connect()
#    cursor=conn.cursor()
#    cursor.execute(sql)
#    conn.commit()
    
#    return render_template("empleados/index.html")

#if __name__=="__main__":
#    app.run(debug=True)
    