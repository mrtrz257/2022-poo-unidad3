import json

from pathlib import Path

from Televisor import Televisor
from Heladera import Heladera
from Lavarropa import Lavarropa


class ObjectEncoder:
    def decodificarDiccionario(self, d):
        retorno = None
        if '__class__' not in d:
            retorno = d
        else:
            class_name = d['__class__']
            class_=eval(class_name)
            if class_name=='Manejador':
                aparatos = d['aparatos']
                manejador = class_()
                for i in range(len(aparatos)):
                    unAparato = aparatos[i]
                    class_name=unAparato.pop('__class__')
                    class_ = eval(class_name)
                    atributos = unAparato['__atributos__']
                    unAparato= class_(**atributos)
                    manejador.agregarElemento(unAparato)
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
