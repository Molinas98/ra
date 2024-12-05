from flask_app import app
from flask import render_template, request, redirect, session, flash
import os
from pathlib import Path
from werkzeug.utils import secure_filename
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
from urllib.parse import unquote
from unidecode import unidecode

load_dotenv()
bcrypt = Bcrypt(app)

app.secret_key = 'secret_key'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/admin')
def mostar_admin():
    if not session.get('user_id'):
        return redirect('/')
    return render_template('admin.html')

@app.route('/login')
def mostrar_login():
    return render_template('login.html')

@app.route('/login/process', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if not os.getenv('ADMIN_USER') == request.form.get("usuario"):
            flash("Usuario incorrecto")
            return redirect('/login')
            
        if not bcrypt.check_password_hash(os.getenv('ADMIN_PASS'), request.form['password']):
            flash("Contraseña incorrecta")
            return redirect('/login')
        
        session['user_id'] = 1
        return redirect('/admin')

    else:
        return redirect('/')
    
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/video/update_process', methods=['POST', 'GET'])
def actualizar_video():
    if not session.get('user_id'):
        return redirect('/')
    if request.method=='POST':
        if request.files["imagen"].filename != "":
            EXTENSIONES_PERMITIDAS = set([".mind"])
            file     = request.files['imagen']
            basepath = os.path.dirname (__file__) #La ruta donde se encuentra el archivo actual
            direccion = Path(basepath)

            filename = secure_filename(file.filename) #Nombre original del archivo
                
            #capturando extension del archivo ejemplo: (.png, .jpg)
            extension = os.path.splitext(filename)[1]
            #validando la extension
            if not extension in EXTENSIONES_PERMITIDAS:
                flash("Imagen no válida, la extensión permitida es .mind")
                return redirect('/admin')

            nuevoNombreFile     = "imagen" + extension
            #direccion.parents[0] retrocede una carpeta
            upload_path = os.path.join (direccion.parents[0], 'static', 'files', nuevoNombreFile) 
            file.save(upload_path)

        if request.files["video"].filename != "":
            EXTENSIONES_PERMITIDAS = set([".mp4"])
            file     = request.files['video']
            basepath = os.path.dirname (__file__) #La ruta donde se encuentra el archivo actual
            direccion = Path(basepath)

            filename = secure_filename(file.filename) #Nombre original del archivo
                
            #capturando extension del archivo ejemplo: (.png, .jpg)
            extension = os.path.splitext(filename)[1]
            #validando la extension
            if not extension in EXTENSIONES_PERMITIDAS:
                flash("Video no válido, la extensión permitida es .mp4")
                return redirect('/admin')

            nuevoNombreFile     = 'video' + extension
            #direccion.parents[0] retrocede una carpeta
            upload_path = os.path.join (direccion.parents[0], 'static', 'files', nuevoNombreFile) 
            file.save(upload_path)

        if request.files["imagen"].filename != "" or request.files["video"].filename != "":
            flash("El video ha sido configurado")
            return redirect('/admin')
        else:
            flash("Los campos estan vacios")
            return redirect('/admin')