from flask import Flask, render_template, request, flash
import mariadb

path_ = render_template
app = Flask(__name__)

try:
    conexion = mariadb.connect(
        host = 'localhost',
        user = 'root',
        password = '.UdeG-2811',
        db = 'eddyfoxy',
        autocommit=True
    )

except mariadb.Error as e:
    print('Error al conectarse a la base de datos', e)
    pass

cur = conexion.cursor()

@app.route('/')
def index():
    return path_('/index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        obtener = request.form
        correo = obtener.get('email')
        pw = obtener.get('password')
    
        dbCorreo = "SELECT correo FROM `usuarios`"
        cur.execute(dbCorreo)
        usuarios = cur.fetchall()

        for usuario in usuarios:
            if str(usuario) == f"('{correo}',)":
                correoValidado = True
                break
            else:
                correoValidado = False
        
        myCursor = conexion.cursor()
        dbPW = "SELECT password FROM `usuarios`"
        myCursor.execute(dbPW)
        passwords = myCursor.fetchall()

        for password in passwords:
            if str(password) == f"('{pw}',)":
                pwValidado = True
                break
            else:
                pwValidado = False

        if (correoValidado == True) and (pwValidado == True):
            return path_('login.html')
        
        elif (correoValidado == False) or (pwValidado == False) or ((correoValidado == False) or (pwValidado == False)):
            flash("Datos invalidos", "danger")
       
    return path_('/index.html')

@app.route('/registro', methods=['GET','POST'])
def registro():
    if request.method == 'POST':
        obtener = request.form
        correo = obtener.get('email')
        pw = obtener.get('password')
        confi = obtener.get('confirmar_password')
    
        dataBase = "SELECT correo FROM `usuarios`"
        cur.execute(dataBase)
        usuarios = cur.fetchall()

        for dato in usuarios:
            if str(dato) == f"('{correo}',)":
                correoValidado = False
                break
            else:
                correoValidado = True

        if (pw == confi) and (correoValidado == True):
            clave = obtener.get('password')
            if len(correo) != 0 and len(clave) != 0:
                query = "INSERT INTO `usuarios` (`id`, `correo`, `password`) VALUES (NULL, '"+str(correo)+"', '"+str(clave)+"');"
                cur.execute(query)
                flash("Cuenta creada", "success")

        elif (pw != confi) or (correoValidado == False) or ((pw != confi) and (correoValidado == False)):
            flash("Datos invalidos", "danger")
    
    return path_('/registro.html')

@app.route('/about')
def about():
    return path_('/about.html')

if __name__ == "__main__":
    app.secret_key = 'super secret key' #NECESARIO PARA MANDAR MENSAJES PRIVADOS
    app.run(host='0.0.0.0', port=3110, debug = True) 