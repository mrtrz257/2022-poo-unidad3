import numpy as np
from Flores import Flores
import csv

class ManejadorFlores:
    __arreglo = None
    def __init__(self):
        self.__arreglo = None
    def crearArreglo(self):
        self.__arreglo = np.empty(8, dtype=Flores)
        archivo = open('flores.csv')
        reader = csv.reader(archivo, delimiter=';')
        i = 0
        for fila in reader:
            unaFlor = Flores(fila[0], fila[1], fila[2], fila[3])
            self.__arreglo[i] = unaFlor
            i += 1
        archivo.close()
    def mostrarArreglo(self):
        text = ''
        for elemento in self.__arreglo:
            text += 'Codigo: {} - {}'.format(elemento.getNumero(), elemento.getNombre()) + '\n'
        return text
    def buscarFlor(self, codigo):
        ver = -1
        i = 0
        band = True
        while band and i < len(self.__arreglo):
            if codigo == self.__arreglo[i].getNumero():
                ver = i
                band = False
            i += 1
        return ver
    def getFlor(self, posicion):
        return self.__arreglo[posicion]
    def registrarVenta(self, posicion):
        self.__arreglo[posicion].registraVenta()
    def mostrarFloresMasVendidas(self):
        text = ''
        lista = np.sort(self.__arreglo)[::-1]
        for i in range(5):
            text += '{}\n'.format(lista[i].getNombre())
        return text
