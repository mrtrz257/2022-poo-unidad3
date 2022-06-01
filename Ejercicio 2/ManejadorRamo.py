from Ramo import Ramo
#from Flores import Flores

class ManejadorRamo:
    __lista = None
    __indice = -1
    def __init__(self):
        self.__lista = []
    def __str__(self):
        return '{}'.format(self.__lista)
    def CrearRamo(self, tam='', flores=None, cantidad = 1):
        self.__indice += 1
        unRamo = Ramo(tam, flores, cantidad)
        self.__lista.append(unRamo)
        return self.__indice
    def agregarFlorARamo(self, indice, flor):
        self.__lista[indice].addFlor(flor)
    def mostrarRamo(self):
        text = ''
        for elemento in self.__lista:
            text += '{}'.format(elemento) + '\n'
        return text
    def mostrarRamoSegunTamano(self, tamanio):
        text = ''
        for elemento in self.__lista:
            if tamanio == elemento.getTamanio():
                text += '{}\n'.format(elemento)
        return text
    def mostrarFlores(self):
        text = ''
        for elemento in self.__lista:
            text += '{}\n'.format(elemento.getFlor())
        return text
