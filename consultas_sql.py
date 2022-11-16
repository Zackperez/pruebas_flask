from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

CORS(app)
# Mysql Connection
app.config['MYSQL_HOST'] = 'bd-sbr-ia.ctl0hwzog7zq.us-east-1.rds.amazonaws.com' 
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'Zacksykes.2018'
app.config['MYSQL_DB'] = 'sistema_de_reglas'
mysql = MySQL(app)

class Consultas_SQL:
    def recibir_usuario_info():
        try:
            cur = mysql.connection.cursor()
            cur.execute('SELECT * FROM Usuario')
            rv = cur.fetchall()
            cur.close()

            payload = []
            usuarios_contenido = {} 
            for result in rv:
                usuarios_contenido = {'id del usuario':result[0], 'id_preguntas': result[1]}
                payload.append(usuarios_contenido)
            return jsonify(payload)
        except Exception as e:
            print(e)
            return print("ocurrio un error")