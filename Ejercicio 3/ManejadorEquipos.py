import numpy as np
from Equipo import Equipo

class ManejadorEquipos:
    __arreglo = None
    __i = 0
    __dimension = 0
    def __init__(self):
        self.__arreglo = np.empty(self.__dimension, dtype=Equipo)
    def setDimensionArreglo(self, dimension):   #Modifica la dimension del arreglo
        self.__dimension = dimension
        self.__arreglo.resize(self.__dimension)
    def agregarArregloEquipos(self, unEquipo):  #Agrega objetos de la clase equipo al arreglo
        self.__arreglo[self.__i] = unEquipo
        self.__i += 1
    def agregarContrato(self, posicion, contrato):  #Registra un contrato
        self.__arreglo[posicion].crearContrato(contrato)
    def mostrarEquipos(self):   #Muestra todos los equipos del arreglo
        text = ''
        for elemento in self.__arreglo:
            text += '{} - {}\n'.format(elemento.getNombre(), elemento.getCiudad())
        return text
    def buscarEquipo(self, equipo):  #Busca un equipo segun su nombre, retorna su posicion o -1 si no se encuentra
        ver = -1
        i = 0
        band = True
        while band and i<len(self.__arreglo):
            if equipo == self.__arreglo[i].getNombre():
                ver = i
                band = False
            i += 1
        return ver
    def convertirFecha(self, fecha):    #Convierte la cadena de las fechas de los contratos en una lista con numeros enteros
        lista = []
        split = fecha.split('/')
        for elemento in split:
            lista.append(int(elemento))
        return lista
    def contratosSeisMeses(self, posicion):     #Retorna un texto con los contratos que terminan en 6 meses
        texto = ''
        for elemento in self.__arreglo[posicion].getContratos():
            fechaInicio = self.convertirFecha(elemento.getFechaInicio())
            fechaFin = self.convertirFecha(elemento.getFechaFin())
            if fechaInicio[2]==fechaFin[2]:
                diferencia = fechaFin[1] - fechaInicio[1]
                if diferencia == 6:
                    texto += '{}\n'.format(elemento.getJugador())
        return texto
    def getEquipo(self, equip):     #Retorna un equipo
        return self.__arreglo[equip]
    def ImporteTotal(self, posicion):   #Calcula el importe de sueldos de un equipo
        acum = 0.0
        for elemento in self.__arreglo[posicion].getContratos():
            acum += elemento.getPago()
        return acum