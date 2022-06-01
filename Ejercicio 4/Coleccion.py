
import numpy as np
from Calefactor import Calefactor

class Coleccion:
    __arreglo = None
    __i = 0
    def __init__(self):
        self.__i = 0
        self.__arreglo = np.empty(0, dtype=Calefactor)
    def __str__(self):
        return '{}'.format(self.__arreglo)
    def crearArreglo(self, tamanio):
        self.__arreglo.resize(tamanio)
    def agregarCalefactor(self, unCalefactor):
        self.__arreglo[self.__i] = unCalefactor
        self.__i += 1
    def mostrarArreglo(self):
        text = ''
        for elemento in self.__arreglo:
            text += '{}/{}\n'.format(elemento.getMarca(), elemento.getModelo())
        return text