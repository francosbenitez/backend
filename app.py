from flask import Flask                             
from flask import render_template, request                   
from flaskext.mysql import MySQL                    

app = Flask(__name__)                               
mysql = MySQL()                                     
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='1234'
app.config['MYSQL_DATABASE_BD']='sistema'
mysql.init_app(app)                                 

@app.route("/")                                     
def index():
    sql="INSERT INTO `sistema`.`pacientes` (`id`, `nombre`, `correo`, `foto`) VALUES (NULL, 'Juan Pablo', 'juanpablo@gmail.com', 'juanpablo.jpg');"
    conn=mysql.connect()                            
    cursor=conn.cursor()                            
    cursor.execute(sql)                             
    conn.commit()                                   
    return render_template("pacientes/index.html")  

@app.route('/create') 
def create(): 
    return render_template('pacientes/create.html')

@app.route("/store", methods=["POST"])
def storage():
    _nombre=request.form['txtNombre'] 
    _correo=request.form['txtCorreo'] 
    _foto=request.files['txtFoto']
    sql = "INSERT INTO `sistema`.`pacientes` (`id`, `nombre`, `correo`, `foto`) VALUES (NULL, %s, %s, %s);" 
    datos=(_nombre,_correo,_foto.filename)
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, datos)                      
    conn.commit()
    return render_template("pacientes/index.html")

if __name__=="__main__":                             
    app.run(debug=True)                             

