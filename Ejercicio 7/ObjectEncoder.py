import json

from pathlib import Path

from Investigador import Investigador
from Docente import Docente
from PersonalDeApoyo import PersonalDeApoyo
from DocenteInvestigador import DocenteInvestigador

class ObjectEncoder:
    def decodificarDiccionario(self, d):
        retorno = None
        if '__class__' not in d:
            retorno = d
        else:
            class_name = d['__class__']
            class_=eval(class_name)
            if class_name=='Manejador':
                personal = d['Personal']
                manejador = class_()
                for i in range(len(personal)):
                    unEmpleado = personal[i]
                    class_name=unEmpleado.pop('__class__')
                    class_ = eval(class_name)
                    atributos = unEmpleado['__atributos__']
                    unEmpleado= class_(**atributos)
                    manejador.agregarElemento(unEmpleado)
                retorno = manejador
        return retorno
    def guardarJSONArchivo(self, diccionario, archivo):
        with Path(archivo).open('w', encoding = 'UTF-8') as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()
    def leerJSONArchivo(self, archivo):
        with Path(archivo).open(encoding='UTF-8') as fuente:
            diccionario = json.load(fuente)
            fuente.close()
            return diccionario
    def convertirTextoADiccionario(self, texto):
        return json.loads(texto)
