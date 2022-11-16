import json
from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin

from random import choice

app = Flask(__name__)

CORS(app)
# Mysql Connection
app.config['MYSQL_HOST'] = 'bd-sbr-ia.ctl0hwzog7zq.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'Zacksykes.2018'
app.config['MYSQL_DB'] = 'sistema_de_reglas'
mysql = MySQL(app)

respuesta_obtenida = []
datos_usuario_temporal = []


@app.route('/')
def bienvenida():
    return jsonify({"bienvenida": "hola"})


@app.route("/agregar_usuario_temporal", methods=['POST'])
def agregar_usuario_temporal():
    datos_usuario = {
        'nombre': request.json['Nombre'],
        'apellido': request.json['Apellido'],
        'respuesta_abdominal': request.json['Respuesta_abdominal'],
        'respuesta_diarrea': request.json['Respuesta_diarrea'],
        'respuesta_estrenimiento': request.json['Respuesta_estrenimiento'],
        'respuesta_acidez': request.json['Respuesta_acidez'],
        'respuesta_vomitos': request.json['Respuesta_vomitos'],
    }

    datos_usuario_temporal.append(datos_usuario)

    Nombre = datos_usuario['nombre']
    Apellido = datos_usuario['apellido']
    Respuesta_abdominal = datos_usuario['respuesta_abdominal']
    Respuesta_diarrea = datos_usuario['respuesta_diarrea']
    Respuesta_estrenimiento = datos_usuario['respuesta_estrenimiento']
    Respuesta_acidez = datos_usuario['respuesta_acidez']
    Respuesta_vomitos = datos_usuario['respuesta_vomitos']
    Diagnostico_final= sbr()

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO Usuario_Respuestas (Nombre, Apellido, Respuesta_abdominal, Respuesta_diarrea, Respuesta_estrenimiento, Respuesta_acidez, Respuesta_vomitos, Diagnostico_final) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", (Nombre,Apellido,Respuesta_abdominal,Respuesta_diarrea,Respuesta_estrenimiento ,Respuesta_acidez,Respuesta_vomitos, Diagnostico_final))
    #cur.execute("INSERT INTO Usuario (Nombre, Apellido) VALUES (%s,%s)", (Nombre, Apellido))
    #print("Insercion de usuario, exitosa")
    #cur.execute("INSERT INTO Respuestas (Respuesta_abdominal, Respuesta_diarrea, Respuesta_estrenimiento, Respuesta_acidez, Respuesta_vomitos, Diagnostico_final) VALUES (%s,%s,%s,%s,%s,%s)", (Respuesta_abdominal,Respuesta_diarrea,Respuesta_estrenimiento ,Respuesta_acidez,Respuesta_vomitos, Diagnostico_final))
    #print("Insercion de respuestas, exitosa")
    cur.close()
    mysql.connection.commit()
    print("Datos añadidos a la BD ")
    return jsonify({"informacion":"Registro exitoso del usuario y sus respuestas"})


@app.route("/mostrar_usuario_temporal")
def mostrar_usuario_temporal():
    print(request.get_json())
    return 'creando usuario temporal'

from sistema_basado_reglas.sistemadereglas import *
from sistema_basado_reglas.reglas import *
from sistema_basado_reglas.sbr_respuestas import *

def sbr():

    engine = sistemadereglas()

    engine.reset()

    print(datos_usuario_temporal)
    print(type(datos_usuario_temporal))
    lista = datos_usuario_temporal[0]
    Respuesta_abdominal = lista['respuesta_abdominal']
    Respuesta_diarrea = lista['respuesta_diarrea']
    Respuesta_estrenimiento = lista['respuesta_estrenimiento']
    Respuesta_acidez = lista['respuesta_acidez']
    Respuesta_vomitos = lista['respuesta_vomitos']

    engine.declare(reglas(resp_abdominal = Respuesta_abdominal))
    engine.declare(reglas(resp_diarrea = Respuesta_diarrea))
    engine.declare(reglas(resp_estrenimiento = Respuesta_estrenimiento))
    engine.declare(reglas(resp_acidez = Respuesta_acidez))
    engine.declare(reglas(resp_vomitos = Respuesta_vomitos))

    engine.run()

    respuesta_sbr = engine.lista_respuestas[0]

    return respuesta_sbr


if __name__ == '__main__':
    app.run(debug = True, port = 4000)