#librerias importadas
from flask import Flask, render_template, request  
from flask_mysqldb import MySQL
import bcrypt

app = Flask(__name__)

#datos requeridos para la base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Noobmaster64'
app.config['MYSQL_DB'] = 'sagastore_registro'

mysql = MySQL(app)

#en esta ruta se mostrara el formulario
@app.route('/')
def formulario():
    return render_template('register.html')

#aqui se prcesa el formulario
@app.route('/registro', methods=['POST']) #ruta para la aplicacion flask
def registrar():
    nombre = request.form['nombre']
    email = request.form['email']
    contrasena = request.form['password']

    #encriptar contraseña para volverla segura
    encriptar = bcrypt.hashpw(contrasena.encode('utf-8'), bcrypt.gensalt())

    #insertar de database

    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO usuario(nombre,email,password_) VALUES (%s, %s, %s)', (nombre,email,encriptar))
    # %s funcionan como placeholders

    mysql.connection.commit()
    cursor.close()

    return render_template('main.html', nombre=nombre)

if __name__ == '__main__':
    app.run(debug=True)
