import numpy as np
from Flores import Flores
import csv

class ManejadorFlores:
    __arreglo = None
    def __init__(self):
        self.__arreglo = None
    def crearArreglo(self):         #Crea un arreglo, lee el archivo y almacena los objetos de la clase flores
        self.__arreglo = np.empty(8, dtype=Flores)
        archivo = open('flores.csv')
        reader = csv.reader(archivo, delimiter=';')
        i = 0
        for fila in reader:
            unaFlor = Flores(fila[0], fila[1], fila[2], fila[3])
            self.__arreglo[i] = unaFlor
            i += 1
        archivo.close()
    def mostrarArreglo(self):       #Muestra el numero y nombre de todas las flores del arreglo
        text = ''
        for elemento in self.__arreglo:
            text += 'Codigo: {} - {}'.format(elemento.getNumero(), elemento.getNombre()) + '\n'
        return text
    def buscarFlor(self, codigo):   #Busca una flor segun un codigo ingresado, retorna la posicion en el arreglo o -1 si no se encuentra
        ver = -1
        i = 0
        band = True
        while band and i < len(self.__arreglo):
            if codigo == self.__arreglo[i].getNumero():
                ver = i
                band = False
            i += 1
        return ver
    def getFlor(self, posicion):        #Retorna una flor del arreglo segun su posicion
        return self.__arreglo[posicion]
    def registrarVenta(self, posicion):    #Cuenta una venta, que se suma al atributo venta en la clase Flor
        self.__arreglo[posicion].registraVenta()
    def mostrarFloresMasVendidas(self):     #Ordena el arreglo segun las ventas y muestra las 5 flores mas vendidas
        text = ''
        lista = np.sort(self.__arreglo)[::-1]
        for i in range(5):
            text += '{}\n'.format(lista[i].getNombre())
        return text
