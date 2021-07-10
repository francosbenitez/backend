from flask import Flask                             # import Flask
from flask import render_template                   # render for templates
from flaskext.mysql import MySQL

app = Flask(__name__)                               # create the application
@app.route("/")                                     # routing so that the user enters the root
def index():
    return render_template("pacientes/index.html")  # identify the folder and the html file

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
    