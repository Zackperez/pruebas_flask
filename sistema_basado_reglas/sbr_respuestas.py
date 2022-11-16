from sistema_basado_reglas.sistemadereglas import *

class sbr_respuestas():

    def __init__(self,respuesta):
        self.respuesta_de_aca = respuesta

    def llenar_respuesta(self,respuesta):
        self.respuesta_de_aca = respuesta

    def devolver_respuesta(self):
        print(self.respuesta_de_aca)