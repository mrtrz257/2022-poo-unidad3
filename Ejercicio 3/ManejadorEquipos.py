import numpy as np
from Equipo import Equipo

class ManejadorEquipos:
    __arreglo = None
    __i = 0
    __dimension = 0
    def __init__(self):
        self.__arreglo = np.empty(self.__dimension, dtype=Equipo)
    def setDimensionArreglo(self, dimension):
        self.__dimension = dimension
        self.__arreglo.resize(self.__dimension)
    def agregarArregloEquipos(self, unEquipo):
        self.__arreglo[self.__i] = unEquipo
        self.__i += 1
    def agregarContrato(self, posicion, contrato):
        self.__arreglo[posicion].crearContrato(contrato)
    def mostrarEquipos(self):
        text = ''
        for elemento in self.__arreglo:
            text += '{} - {}\n'.format(elemento.getNombre(), elemento.getCiudad())
        return text
    def buscarEquipo(self, equipo):
        ver = -1
        i = 0
        band = True
        while band and i<len(self.__arreglo):
            if equipo == self.__arreglo[i].getNombre():
                ver = i
                band = False
            i += 1
        return ver
    def convertirFecha(self, fecha):
        lista = []
        split = fecha.split('/')
        for elemento in split:
            lista.append(int(elemento))
        return lista
    def contratosSeisMeses(self, posicion):
        texto = ''
        for elemento in self.__arreglo[posicion].getContratos():
            fechaInicio = self.convertirFecha(elemento.getFechaInicio())
            fechaFin = self.convertirFecha(elemento.getFechaFin())
            if fechaInicio[2]==fechaFin[2]:
                diferencia = fechaFin[1] - fechaInicio[1]
                if diferencia == 6:
                    texto += '{}\n'.format(elemento.getJugador())
        return texto
    def getEquipo(self, equip):
        return self.__arreglo[equip]
    def ImporteTotal(self, posicion):
        acum = 0.0
        for elemento in self.__arreglo[posicion].getContratos():
            acum += elemento.getPago()
        return acum