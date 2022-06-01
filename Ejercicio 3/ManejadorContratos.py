import csv

import numpy as np
from Contrato import Contrato

class ManejadorContratos:
    __arreglo = None
    __i = 0
    __dimension = 0
    def __init__(self):
        self.__arreglo = np.empty(self.__dimension, dtype=Contrato)
    def setDimensionArreglo(self, dimension):
        self.__dimension = dimension
        self.__arreglo.resize(self.__dimension)
    def agregarArregloContratos(self, unContrato):
        self.__arreglo[self.__i] = unContrato
        self.__i += 1
    def mostrarContratos(self):
        for elemento in self.__arreglo:
            print(elemento)
    def buscarJugador(self, dni):
        band = True
        ver = -1
        i = 0
        while band and i < len(self.__arreglo):
            jugador = self.__arreglo[i].getJugador()
            if jugador.getDNI() == dni:
                ver = i
                band = False
            i += 1
        return ver
    def buscarEquipo(self, equipo):
        band = True
        ver = -1
        i = 0
        while band and i < len(self.__arreglo):
            buscaEquipo = self.__arreglo[i].getEquipo()
            if buscaEquipo.getNombre() == equipo:
                ver = i
                band = False
            i += 1
        return ver
    def muestraEquipoYContrato(self, posicion):
        text = ''
        equipo = self.__arreglo[posicion].getEquipo()
        text += '{}\n'.format(equipo)
        text += 'Fecha de Finalización: {}'.format(self.__arreglo[posicion].getFechaFin())
        return text
    def guardarArchivoContratos(self):
        with open('contratos.csv', 'w', newline= '') as archivo:
            writer = csv.writer(archivo, delimiter=';')
            for elemento in self.__arreglo:
                if elemento is not None:
                    equipo = elemento.getEquipo()
                    jugador = elemento.getJugador()
                    writer.writerow([jugador.getDNI(), equipo.getNombre(), elemento.getFechaInicio(), elemento.getFechaFin(), elemento.getPago()])
        archivo.close()