from flask import Flask                             
from flask import render_template, request, redirect                   
from flaskext.mysql import MySQL                    
from datetime import datetime

app = Flask(__name__)                               
mysql = MySQL()                                     
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='1234'
app.config['MYSQL_DATABASE_BD']='sistema'
mysql.init_app(app)                                 

@app.route("/")                                     
def index():
    sql = "SELECT * FROM `sistema`.`pacientes`;"
    conn=mysql.connect()                            
    cursor=conn.cursor()                            
    cursor.execute(sql)                             
    pacientes = cursor.fetchall()
    print(pacientes)
    conn.commit()                                   
    return render_template("pacientes/index.html", pacientes = pacientes)  

@app.route("/destroy/<int:id>")
def destroy(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM `sistema`.`pacientes` WHERE id=%s", (id))
    conn.commit()
    return redirect("/")

@app.route("/edit/<int:id>")
def edit(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM `sistema`.`pacientes` WHERE ID=%s", (id))
    pacientes = cursor.fetchall() 
    conn.commit()
    return render_template("pacientes/edit.html", pacientes = pacientes)

@app.route('/create') 
def create(): 
    return render_template('pacientes/create.html')

@app.route("/store", methods=["POST"])
def storage():
    _nombre = request.form['txtNombre'] 
    _correo = request.form['txtCorreo'] 
    _foto = request.files['txtFoto']
    now = datetime.now()
    tiempo = now.strftime("%Y%H%M%S")
    if _foto.filename != "":
        nuevoNombreFoto = tiempo + _foto.filename
        _foto.save("uploads/" + nuevoNombreFoto)
    sql = "INSERT INTO `sistema`.`pacientes` (`id`, `nombre`, `correo`, `foto`) VALUES (NULL, %s, %s, %s);" 
    datos = (_nombre, _correo, nuevoNombreFoto)
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, datos)                      
    conn.commit()
    return render_template("pacientes/index.html")

if __name__=="__main__":                             
    app.run(debug=True)                             

