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
        'id_usuario': request.json['Id_usuario'],
        'nombre': request.json['Nombre'],
        'apellido': request.json['Apellido'],
        'respuesta_abdominal': request.json['Respuesta_abdominal'],
        'respuesta_diarrea': request.json['Respuesta_diarrea'],
        'respuesta_estrenimiento': request.json['Respuesta_estrenimiento'],
        'respuesta_acidez': request.json['Respuesta_acidez'],
        'respuesta_vomitos': request.json['Respuesta_vomitos'],
    }

    datos_usuario_temporal.append(datos_usuario)
    Id_usuario = datos_usuario['id_usuario']
    Nombre = datos_usuario['nombre']
    Apellido = datos_usuario['apellido']
    Respuesta_abdominal = datos_usuario['respuesta_abdominal']
    Respuesta_diarrea = datos_usuario['respuesta_diarrea']
    Respuesta_estrenimiento = datos_usuario['respuesta_estrenimiento']
    Respuesta_acidez = datos_usuario['respuesta_acidez']
    Respuesta_vomitos = datos_usuario['respuesta_vomitos']
    Diagnostico_final= sbr()

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO Usuario_Respuestas (Id_usuario, Nombre, Apellido, Respuesta_abdominal, Respuesta_diarrea, Respuesta_estrenimiento, Respuesta_acidez, Respuesta_vomitos, Diagnostico_final) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)", (Id_usuario, Nombre, Apellido,Respuesta_abdominal,Respuesta_diarrea,Respuesta_estrenimiento ,Respuesta_acidez,Respuesta_vomitos, Diagnostico_final))
    cur.close()
    mysql.connection.commit()
    print("Datos añadidos a la BD ")
    return jsonify({"informacion":"Registro exitoso del usuario y sus respuestas"})

@app.route("/respuesta_sbr/<id>", methods = ['GET'])
def respuesta_sbr(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM Usuario_Respuestas WHERE Id_Usuario LIKE %s',[id])
        #cur.execute( "SELECT * FROM records WHERE email LIKE %s", [search] )
        rv = cur.fetchall()
        cur.close()
        payload = []
        content = {}
        for result in rv:
            content = {"id_usuario":result[0],"Nombre":result[1],"Apellido":result[2],"Respuesta_abdominal":result[3],"Respuesta_diarrea":result[4],"Respuesta_estrenimiento":result[5],"Respuesta_acidez":result[6],"Respuesta_vomitos":result[7],"Diagnostico_final":result[8]}
            payload.append(content)
            content = {}
        #respuesta_obtenida.append(sbr(rv))
        return jsonify(payload)
    except Exception as e:
        print(e)
        return jsonify({"informacion":e})

from sistema_basado_reglas.sistemadereglas import *
from sistema_basado_reglas.reglas import *
from sistema_basado_reglas.sbr_respuestas import *

def sbr():

    engine = sistemadereglas()

    engine.reset()

    #print(datos_usuario_temporal)
    #print(type(datos_usuario_temporal))
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

    lista = []

    return respuesta_sbr


if __name__ == '__main__':
    app.run(debug = True, port = 4000)