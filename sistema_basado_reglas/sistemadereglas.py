from sistema_basado_reglas.reglas import *
from sistema_basado_reglas.sbr_respuestas import *



class sistemadereglas(KnowledgeEngine):

    lista_respuestas = []

    @Rule(AND(reglas(resp_abdominal="Si")), (reglas(resp_diarrea="Si")), (reglas(resp_estrenimiento="No")), (reglas(resp_acidez="No")), (reglas(resp_vomitos="Si")))
    def m1(self):
        respuesta = "Logrado, DALLA DALLA"
        self.lista_respuestas.append(respuesta)
