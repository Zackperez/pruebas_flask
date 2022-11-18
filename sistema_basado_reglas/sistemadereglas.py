from sistema_basado_reglas.reglas import *

class sistemadereglas(KnowledgeEngine):

    lista_respuestas = []

    @Rule(AND(reglas(resp_vomitos="Si")), (reglas(resp_abdominal="Si")), (reglas(resp_diarrea="Si")), (reglas(resp_acidez="Si")), (reglas(resp_estrenimiento="Si")))
    def m1(self):
        respuesta = "Tiene una enfermedad en el sistema digestivo, tienes que acudir a un médico"
        self.lista_respuestas.append(respuesta)

    @Rule(AND(reglas(resp_vomitos="Si")), (reglas(resp_abdominal="Si")), (reglas(resp_diarrea="Si")), (reglas(resp_acidez="Si")), (reglas(resp_estrenimiento="No")))
    def m2(self):
        respuesta = "Es posible que tengas un problema en el sistema digestivo"
        self.lista_respuestas.append(respuesta)

    @Rule(AND(reglas(resp_vomitos="Si")), (reglas(resp_abdominal="Si")), (reglas(resp_diarrea="Si")), (reglas(resp_acidez="No")), (reglas(resp_estrenimiento="Si")))
    def m3(self):
        respuesta = "Puede que tengas una enfermedad celíaca"
        self.lista_respuestas.append(respuesta)

    @Rule(AND(reglas(resp_vomitos="Si")), (reglas(resp_abdominal="Si")), (reglas(resp_diarrea="Si")), (reglas(resp_acidez="No")), (reglas(resp_estrenimiento="No")))
    def m4(self):
        respuesta = "Posibilidad de una enfermedad celíaca."
        self.lista_respuestas.append(respuesta)

    @Rule(AND(reglas(resp_vomitos="Si")), (reglas(resp_abdominal="Si")), (reglas(resp_diarrea="No")), (reglas(resp_acidez="Si")), (reglas(resp_estrenimiento="Si")))
    def m5(self):
        respuesta = "Reflujos Gastroesofágico."
        self.lista_respuestas.append(respuesta)

    @Rule(AND(reglas(resp_vomitos="Si")), (reglas(resp_abdominal="Si")), (reglas(resp_diarrea="No")), (reglas(resp_acidez="Si")), (reglas(resp_estrenimiento="No")))
    def m6(self):
        respuesta = "Posiblemente tienes una enfermedad de Crohn"
        self.lista_respuestas.append(respuesta)

    @Rule(AND(reglas(resp_vomitos="Si")), (reglas(resp_abdominal="Si")), (reglas(resp_diarrea="No")), (reglas(resp_acidez="No")), (reglas(resp_estrenimiento="Si")))
    def m7(self):
        respuesta = "Posiblemente enfermedad celíaca."
        self.lista_respuestas.append(respuesta)

    @Rule(AND(reglas(resp_vomitos="Si")), (reglas(resp_abdominal="Si")), (reglas(resp_diarrea="No")), (reglas(resp_acidez="No")), (reglas(resp_estrenimiento="No")))
    def m8(self):
        respuesta = "Posiblemente Enfermedad gastroesofágico."
        self.lista_respuestas.append(respuesta)

    @Rule(AND(reglas(resp_vomitos="Si")), (reglas(resp_abdominal="No")), (reglas(resp_diarrea="Si")), (reglas(resp_acidez="Si")), (reglas(resp_estrenimiento="Si")))
    def m9(self):
        respuesta = "Enfermedad de reflujo gastroesofágico."
        self.lista_respuestas.append(respuesta)

    @Rule(AND(reglas(resp_vomitos="Si")), (reglas(resp_abdominal="No")), (reglas(resp_diarrea="Si")), (reglas(resp_acidez="Si")), (reglas(resp_estrenimiento="No")))
    def m10(self):
        respuesta = "Posiblemente Enfermedad de reflujo gastroesofágico."
        self.lista_respuestas.append(respuesta)

    @Rule(AND(reglas(resp_vomitos="Si")), (reglas(resp_abdominal="No")), (reglas(resp_diarrea="Si")), (reglas(resp_acidez="No")), (reglas(resp_estrenimiento="Si")))
    def m11(self):
        respuesta = "Enfermedad celíaca"
        self.lista_respuestas.append(respuesta)

    @Rule(AND(reglas(resp_vomitos="Si")), (reglas(resp_abdominal="No")), (reglas(resp_diarrea="Si")), (reglas(resp_acidez="No")), (reglas(resp_estrenimiento="No")))
    def m12(self):
        respuesta = "No es posible dar una respuesta precisa."
        self.lista_respuestas.append(respuesta)

    @Rule(AND(reglas(resp_vomitos="Si")), (reglas(resp_abdominal="No")), (reglas(resp_diarrea="No")), (reglas(resp_acidez="Si")), (reglas(resp_estrenimiento="Si")))
    def m13(self):
        respuesta = "Posiblemente Enfermedad del reflujo gastroesofágico."
        self.lista_respuestas.append(respuesta)

    @Rule(AND(reglas(resp_vomitos="Si")), (reglas(resp_abdominal="No")), (reglas(resp_diarrea="No")), (reglas(resp_acidez="Si")), (reglas(resp_estrenimiento="No")))
    def m14(self):
        respuesta = "Posiblemente enfermedad gastroesofágico."
        self.lista_respuestas.append(respuesta)

    @Rule(AND(reglas(resp_vomitos="Si")), (reglas(resp_abdominal="No")), (reglas(resp_diarrea="No")), (reglas(resp_acidez="No")), (reglas(resp_estrenimiento="Si")))
    def m15(self):
        respuesta = "No es posible dar una respuesta precisa."
        self.lista_respuestas.append(respuesta)

    @Rule(AND(reglas(resp_vomitos="Si")), (reglas(resp_abdominal="No")), (reglas(resp_diarrea="No")), (reglas(resp_acidez="No")), (reglas(resp_estrenimiento="No")))
    def m16(self):
        respuesta = "Los vómitos puede dar por la resaca, el embarazo, comer en exceso o el mareo por movimiento."
        self.lista_respuestas.append(respuesta)

    @Rule(AND(reglas(resp_vomitos="No")), (reglas(resp_abdominal="Si")), (reglas(resp_diarrea="Si")), (reglas(resp_acidez="Si")), (reglas(resp_estrenimiento="Si")))
    def m17(self):
        respuesta = "Posiblemente reflujos gastroesofágico."
        self.lista_respuestas.append(respuesta)

    @Rule(AND(reglas(resp_vomitos="No")), (reglas(resp_abdominal="Si")), (reglas(resp_diarrea="Si")), (reglas(resp_acidez="Si")), (reglas(resp_estrenimiento="No")))
    def m18(self):
        respuesta = "Posiblemente reflujos gastroesofágico."
        self.lista_respuestas.append(respuesta)

    @Rule(AND(reglas(resp_vomitos="No")), (reglas(resp_abdominal="Si")), (reglas(resp_diarrea="Si")), (reglas(resp_acidez="No")), (reglas(resp_estrenimiento="Si")))
    def m19(self):
        respuesta = "Posiblemente enfermedad celíaca."
        self.lista_respuestas.append(respuesta)

    @Rule(AND(reglas(resp_vomitos="No")), (reglas(resp_abdominal="Si")), (reglas(resp_diarrea="Si")), (reglas(resp_acidez="No")), (reglas(resp_estrenimiento="No")))
    def m20(self):
        respuesta = "No es posible dar una respuesta precisa."
        self.lista_respuestas.append(respuesta)

    @Rule(AND(reglas(resp_vomitos="No")), (reglas(resp_abdominal="Si")), (reglas(resp_diarrea="No")), (reglas(resp_acidez="Si")), (reglas(resp_estrenimiento="Si")))
    def m21(self):
        respuesta = "Posiblemente reflujos gastroesofágico."
        self.lista_respuestas.append(respuesta)

    @Rule(AND(reglas(resp_vomitos="No")), (reglas(resp_abdominal="Si")), (reglas(resp_diarrea="No")), (reglas(resp_acidez="Si")), (reglas(resp_estrenimiento="No")))
    def m22(self):
        respuesta = "No es posible dar una respuesta precisa."
        self.lista_respuestas.append(respuesta)

    @Rule(AND(reglas(resp_vomitos="No")), (reglas(resp_abdominal="Si")), (reglas(resp_diarrea="No")), (reglas(resp_acidez="No")), (reglas(resp_estrenimiento="Si")))
    def m23(self):
        respuesta = "Posiblemente enfermedad celíaca."
        self.lista_respuestas.append(respuesta)

    @Rule(AND(reglas(resp_vomitos="No")), (reglas(resp_abdominal="No")), (reglas(resp_diarrea="No")), (reglas(resp_acidez="No")), (reglas(resp_estrenimiento="No")))
    def m24(self):
        respuesta = "El dolor abdominal puede darse por constipación, gases, comer en exceso, estrés o distensión muscular."
        self.lista_respuestas.append(respuesta)

    @Rule(AND(reglas(resp_vomitos="No")), (reglas(resp_abdominal="No")), (reglas(resp_diarrea="Si")), (reglas(resp_acidez="Si")), (reglas(resp_estrenimiento="Si")))
    def m25(self):
        respuesta = "Posiblemente reflujo gastroesofágico."
        self.lista_respuestas.append(respuesta)

    @Rule(AND(reglas(resp_vomitos="No")), (reglas(resp_abdominal="No")), (reglas(resp_diarrea="Si")), (reglas(resp_acidez="Si")), (reglas(resp_estrenimiento="No")))
    def m26(self):
        respuesta = "No es posible dar una respuesta precisa."
        self.lista_respuestas.append(respuesta)

    @Rule(AND(reglas(resp_vomitos="No")), (reglas(resp_abdominal="No")), (reglas(resp_diarrea="Si")), (reglas(resp_acidez="No")), (reglas(resp_estrenimiento="Si")))
    def m27(self):
        respuesta = "Posiblemente Hemorroides."
        self.lista_respuestas.append(respuesta)

    @Rule(AND(reglas(resp_vomitos="No")), (reglas(resp_abdominal="No")), (reglas(resp_diarrea="Si")), (reglas(resp_acidez="No")), (reglas(resp_estrenimiento="No")))
    def m28(self):
        respuesta = "La Diarrea puede ser ocasionada por un virus o, a veces, comida contaminada."
        self.lista_respuestas.append(respuesta)

    @Rule(AND(reglas(resp_vomitos="No")), (reglas(resp_abdominal="No")), (reglas(resp_diarrea="No")), (reglas(resp_acidez="Si")), (reglas(resp_estrenimiento="Si")))
    def m29(self):
        respuesta = "No es posible dar una respuesta precisa."
        self.lista_respuestas.append(respuesta)

    @Rule(AND(reglas(resp_vomitos="No")), (reglas(resp_abdominal="No")), (reglas(resp_diarrea="No")), (reglas(resp_acidez="Si")), (reglas(resp_estrenimiento="No")))
    def m30(self):
        respuesta = "La acidez se puede dar por comida picante, alcohol, comer demasiado o usar ropa ajustada."
        self.lista_respuestas.append(respuesta)

    @Rule(AND(reglas(resp_vomitos="No")), (reglas(resp_abdominal="No")), (reglas(resp_diarrea="No")), (reglas(resp_acidez="No")), (reglas(resp_estrenimiento="Si")))
    def m31(self):
        respuesta = "El estreñimiento puede dar por  deshidratación, falta de fibra en la dieta, inactividad física o efectos secundarios de medicamentos."
        self.lista_respuestas.append(respuesta)

    @Rule(AND(reglas(resp_vomitos="No")), (reglas(resp_abdominal="No")), (reglas(resp_diarrea="No")), (reglas(resp_acidez="No")), (reglas(resp_estrenimiento="No")))
    def m32(self):
        respuesta = "Estás sano."
        self.lista_respuestas.append(respuesta)

