#FUNCIONAL CON DETALLES

@app.route("/agregar_usuario_temporal", methods=['POST'])
def agregar_usuario_temporal():
    datos_usuario = {
        'nombre': request.json['Nombre'],
        'apellido': request.json['Apellido'],
        'respuesta_abdominal': request.json['Respuesta_abdominal'],
        'respuesta_diarrea': request.json['Respuesta_diarrea'],
        'respuesta_estrenimiento': request.json['Respuesta_estrenimiento'],
        'respuesta_acidez': request.json['Respuesta_acidez'],
        'respuesta_vomitos': request.json['Respuesta_vomitos']
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
    cur.execute("INSERT INTO Usuario (Nombre, Apellido) VALUES (%s,%s)", (Nombre, Apellido))
    print("Insercion de usuario, exitosa")
    cur.execute("INSERT INTO Respuestas (Respuesta_abdominal, Respuesta_diarrea, Respuesta_estrenimiento, Respuesta_acidez, Respuesta_vomitos, Diagnostico_final) VALUES (%s,%s,%s,%s,%s,%s)", (Respuesta_abdominal,Respuesta_diarrea,Respuesta_estrenimiento ,Respuesta_acidez,Respuesta_vomitos, Diagnostico_final))
    print("Insercion de respuestas, exitosa")
    
    cur.close()
    mysql.connection.commit()
    print("Datos añadidos a la BD ")
    return jsonify({"informacion":"Registro exitoso del usuario y sus respuestas"})




@app.route('/get_user_info')
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
        return jsonify({"error":e})

@app.route('/get_all_user_questions') #Muestra todos los registros
def recibir_preguntas_usuario():
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM Preguntas')
        rv = cur.fetchall()
        cur.close()
        payload = []
        content = {"nose":rv}
        for result in rv:
            print({"id_preguntas":result[0],"id_respuestas":result[1],"id_usuario":result[2],"Pregunta 1":result[3],"Pregunta 2":result[4],"Pregunta 3":result[5],"Pregunta 4":result[6],"Pregunta 5":result[7]})
        
        return jsonify(content)
    except Exception as e:
        print(e)
        return jsonify({"error":e})

@app.route('/get_user/<id>',methods=['GET'])
def getAllById(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM Usuario_Respuestas WHERE Id_Usuario = %s', (id))
        rv = cur.fetchall()
        cur.close()
        content = {rv}
        web = {"nose":rv}
        respuesta_obtenida.append(sbr(rv)) #USO
        return jsonify(web)
    except Exception as e:
        print(e)
        return jsonify({"informacion":e})

@app.route('/add_contact', methods=['POST'])
def agregar_respuestas():
    try:
        if request.method == 'POST':
            respuesta1 = request.json['Respuesta_1']
            respuesta2 = request.json['Respuesta_2']       
            respuesta3 = request.json['Respuesta_3']        
            respuesta4 = request.json['Respuesta_4']     
            respuesta5 = request.json['Respuesta_5']

 #INSERT INTO notificacion (id_blog,fecha, notificacion) VALUES  (ultimo_id_blog,fechaAdd, 'Registro Exitoso');
            cur = mysql.connection.cursor()
            respuesta = sbr()
            cur.execute("INSERT INTO Respuestas (Respuesta_1,Respuesta_2,Respuesta_3,Respuesta_4,Respuesta_5) VALUES (%s,%s,%s,%s,%s)", (respuesta1,respuesta2,respuesta3,respuesta4,respuesta5))
            cur.close()
            mysql.connection.commit()
            return jsonify({"informacion":"Registro exitoso de respuestas"})
    except Exception as e:
        print(e)
        return jsonify({"informacion":e})


@app.route('/add_user_json', methods=['POST'])
def add_user_json():
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
    return jsonify(datos_usuario)

@app.route('/show_users_json')
def get_user_json():
    return jsonify(datos_usuario_temporal)

@app.route('/add_user', methods=['POST'])
def agregar_usuario():
    try:
        if request.method == 'POST':
            Nombre = request.json['Nombre']
            Apellido = request.json['Apellido']
            Respuesta_abdominal= request.json['Respuesta_abdominal']
            Respuesta_diarrea = request.json['Respuesta_diarrea']
            Respuesta_estrenimiento = request.json['Respuesta_estrenimiento']
            Respuesta_acidez = request.json['Respuesta_acidez']
            Respuesta_vomitos = request.json['Respuesta_vomitos']

            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO Usuario_Respuestas (Nombre, Apellido, Respuesta_abdominal, Respuesta_diarrea, Respuesta_estrenimiento, Respuesta_acidez, Respuesta_vomitos) VALUES (%s,%s,%s,%s,%s,%s,%s)", (Nombre,Apellido,Respuesta_abdominal,Respuesta_diarrea,Respuesta_estrenimiento ,Respuesta_acidez,Respuesta_vomitos))
            cur.close()
            mysql.connection.commit()
            return jsonify({"informacion":"Registro exitoso del usuario y sus respuestas"})
        
    except Exception as e:
        print(e)
        return jsonify({"informacion":e})


@app.route('/add_user_bd', methods=['POST'])
def agregar_usuario_bd():
    try:
            Nombre = datos_usuario_temporal[0]
            Apellido = datos_usuario_temporal[1]
            Respuesta_abdominal= datos_usuario_temporal[2]
            Respuesta_diarrea = datos_usuario_temporal[3]
            Respuesta_estrenimiento = datos_usuario_temporal[4]
            Respuesta_acidez = datos_usuario_temporal[5]
            Respuesta_vomitos = datos_usuario_temporal[6]
            print(respuesta_obtenida = sbr())
            cur = mysql.connection.cursor() 
            cur.execute("INSERT INTO Usuario_Respuestas (Nombre, Apellido, Respuesta_abdominal, Respuesta_diarrea, Respuesta_estrenimiento, Respuesta_acidez, Respuesta_vomitos) VALUES (%s,%s,%s,%s,%s,%s,%s)", (Nombre,Apellido,Respuesta_abdominal,Respuesta_diarrea,Respuesta_estrenimiento ,Respuesta_acidez,Respuesta_vomitos))
            cur.close()
            mysql.connection.commit()
            return jsonify({"informacion":"Registro exitoso del usuario y sus respuestas"})
        
    except Exception as e:
        print(e)
        return jsonify({"informacion":e})