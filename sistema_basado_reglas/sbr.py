from sistemadereglas import *
from random import choice

engine = sistemadereglas()

def sbr_preguntas():
    
    engine.reset()

    engine.declare(reglas(pj_level=choice([str(pj85_respuesta.upper())])))

    engine.declare(reglas(pj_ilvl=choice([pjilvl_respuesta])))    

    engine.declare(reglas(pj_justicia=choice([pjjusticia_respuesta])))    

    engine.declare(reglas(pj_elites=choice([str(pj_elites_respuesta.upper())])))

    engine.declare(reglas(pj_guild=choice([str(pjguild_respuesta.upper())])))
