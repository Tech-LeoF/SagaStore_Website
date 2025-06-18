from flask import Flask, render_template, request, session
from flask_mysqldb import MySQL
import bcrypt

app = Flask(__name__)
app.secret_key = 'llave'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'JdHaCaRu74916'
app.config['MYSQL_DB'] = 'sagastore_registro'

mysql = MySQL(app)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/acceder', methods=['POST'])
def acceder():
    email = request.form['email']
    password = request.form['password'].encode('utf-8')

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT nombre, password_ FROM usuario  WHERE email = %s", (email,))
    usuario = cursor.fetchone()
    cursor.close()

    if usuario and bcrypt.checkpw(password, usuario[1].encode('utf-8')):
         session['nombre'] = usuario[0]
        return render_template('LandPage.html', nombre=usuario[0])
    else:
        return 'Contraseña o correo incorrectos'
        
@app.route('/ajustes')
def ajustes():
    nombre = session.get('nombre') 
    return render_template('settings.html', nombre = nombre)

if __name__ == '__main__':
    app.run(debug=True)
