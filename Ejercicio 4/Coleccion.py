import numpy as np
from Calefactor import Calefactor
from CalefactorElectrico import CalefactorElectrico
from CalefactorAGas import CalefactorAGas

class Coleccion:
    __arreglo = None
    __i = 0
    __dimension = 0
    def __init__(self):
        self.__arreglo = np.empty(self.__dimension, dtype=Calefactor)
        self.__i = 0
        self.__dimension = 0
    def __str__(self):
        return '{}'.format(self.__arreglo)
    def setDimensionArreglo(self, tamanio):
        self.__dimension = tamanio
        self.__arreglo.resize(self.__dimension)
    def agregarCalefactor(self, unCalefactor):
        if self.__i <= self.__dimension - 1:
            self.__arreglo[self.__i] = unCalefactor
            self.__i += 1
        else:
            dim = self.__dimension + 1
            self.setDimensionArreglo(dim)
            self.__arreglo[self.__i] = unCalefactor
            self.__i += 1
    def mostrarArreglo(self):       #Muestra todos los datos del arreglo
        text = ''
        for elemento in self.__arreglo:
            text += '{}/{}\n'.format(elemento.getMarca(), elemento.getModelo())
        return text
    def mostrarNombreCalefactor(self, posicion):        #Muestra el nombre de 1 calefactor
        return '{}'.format(self.__arreglo[posicion].getCalefactor())
    def mostrarDatosCalefactor(self, posicion):         #Muestra todos los datos de 1 calefactor
        return '{}'.format(self.__arreglo[posicion])
    def calcularCosto(self, posicion, costo, cantidad):     #Calcula el costo total
        costoTotal = (self.__arreglo[posicion].getConsumo()/1000)*cantidad*costo
        return costoTotal
    def calcularConsumoMinimoAGas(self, cantidad, costo):   #Calcula el consumo minimo de los calefactores a gas
        posicion = -1
        min = 1000000000
        for i in range(len(self.__arreglo)):
            if(isinstance(self.__arreglo[i], CalefactorAGas)):
                costoTotal = self.calcularCosto(i, costo, cantidad)
                if costoTotal < min:
                    min = costoTotal
                    posicion = i
        return posicion
    def calcularConsumoMinimoElectrico(self, cantidad, costo):      #Calcula el consumo minimo de los calefactores electricos
        posicion = -1
        min = 1000000000
        for i in range(len(self.__arreglo)):
            if(isinstance(self.__arreglo[i], CalefactorElectrico)):
                costoTotal = self.calcularCosto(i, costo, cantidad)
                if costoTotal < min:
                    min = costoTotal
                    posicion = i
        return posicion
    def calcularConsumoMinimoGeneral(self, cantidad, costo):        #Calcula el consumo minimo de todos los calefactores
        posicion = -1
        min = 1000000000
        for i in range(len(self.__arreglo)):
            costoTotal = self.calcularCosto(i, costo, cantidad)
            if costoTotal < min:
                min = costoTotal
                posicion = i
        return posicion
