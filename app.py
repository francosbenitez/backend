from flask import Flask                             
from flask import render_template, request, redirect, url_for, flash                   
from flaskext.mysql import MySQL                    
from datetime import datetime
import os 
from flask import send_from_directory

app = Flask(__name__)                               
app.secret_key="ClaveSecreta"
mysql = MySQL()                                     
app.config['MYSQL_DATABASE_HOST']='aws-simplified.cfd0h5xpluom.us-east-2.rds.amazonaws.com'
app.config['MYSQL_DATABASE_USER']='admin'
app.config['MYSQL_DATABASE_PASSWORD']='42334770'
app.config['MYSQL_DATABASE_BD']='sistema'
mysql.init_app(app)                                 

folder = os.path.join("uploads")
app.config["folder"] = folder

@app.route("/uploads/<nombreFoto>")
def uploads(nombreFoto):
    return send_from_directory(app.config["folder"], nombreFoto)

@app.route("/")                                     
def index():
    sql = "SELECT * FROM `sistema`.`pacientes`;"
    conn=mysql.connect()                            
    cursor=conn.cursor()                            
    cursor.execute(sql)                             
    pacientes = cursor.fetchall()
    print(pacientes)
    conn.commit()                                   
    return render_template("pacientes/index.html", pacientes=pacientes)  

@app.route("/destroy/<int:id>")
def destroy(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT foto FROM `sistema`.`pacientes` WHERE id=%s", id)
    fila = cursor.fetchall()
    os.remove(os.path.join(app.config["folder"], fila[0][0]))
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

@app.route("/update", methods=["POST"])
def update():
    _nombre = request.form["txtNombre"]
    _correo = request.form["txtCorreo"]
    _foto = request.files["txtFoto"]
    id = request.form["txtID"]
    sql = "UPDATE `sistema`.`pacientes` SET `nombre`=%s, `correo`=%s WHERE id=%s;"
    datos = (_nombre, _correo, id)
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, datos)
    conn.commit()
    now = datetime.now()
    tiempo = now.strftime("%Y%H%M%S")
    if _foto.filename != "":
        nuevoNombreFoto = tiempo + _foto.filename
        _foto.save("uploads/" + nuevoNombreFoto)
        cursor.execute("SELECT foto FROM `sistema`.`pacientes` WHERE id=%s", id)
        #fila = cursor.fetchall()
        #os.remove(os.path.join(app.config["folder"], fila[0][0]))
        cursor.execute("UPDATE `sistema`.`pacientes` SET foto=%s WHERE id=%s", (nuevoNombreFoto, id))
        conn.commit()
    return redirect("/")

@app.route('/create') 
def create(): 
    return render_template('pacientes/create.html')

@app.route("/store", methods=["POST"])
def storage():
    _nombre = request.form['txtNombre'] 
    _correo = request.form['txtCorreo'] 
    _foto = request.files['txtFoto']
    if _nombre == '' or _correo == '' or _foto =='': 
        flash('Recuerda llenar los datos de los campos') 
        return redirect(url_for('create')) 
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
    return redirect('/')

if __name__=="__main__":                             
    app.run(debug=True)                             

