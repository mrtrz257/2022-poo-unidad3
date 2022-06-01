from Facultad import Facultad
import numpy as np
import csv

class ManejadorFacultad:
    __arreglo = None
    def __init__(self):
        self.__arreglo = np.empty(5, dtype= Facultad)
    def crearFacultad(self):        #Abre el archivo y almacena las instancias de la clase Facultad en el arreglo
        archivo = open('Facultades.csv')
        reader = csv.reader(archivo, delimiter=';')
        i = 0
        for fila in reader:
            indice = int(fila[5])
            unaFacultad = Facultad(fila[0], fila[1], fila[2], fila[3], fila[4], indice, reader)  #Manda reader como parametro para crear instancias de la clase Carrera
            self.__arreglo[i] = unaFacultad
            i += 1
        archivo.close()
    def mostrarFacultades(self):    #Muestra Todas las Facultades Almacenadas
        text = ''
        for elemento in self.__arreglo:
            text += '{} {}'.format(elemento.getCodFacultad(), elemento.getNomFacultad()) + '\n'
        return text
    def listarCarreras(self):       #Muestra todas las carreras Almacenadas
        for e in self.__arreglo:
            print(e.mostrarCarreras())
    def DatosCarrera(self, cod):    #Muestra los datos de una carrera segun un codigo de Facultad Ingresado
        text = ''
        band = True
        i = 0
        while band and i < len(self.__arreglo):
            if cod == self.__arreglo[i].getCodFacultad():
                text = self.__arreglo[i].getDatosCarrera()
                band = False
            i += 1
        return text
    def buscarCodigoFacultad(self, carrera):    #Busca el codigo de una facultad segun el nombre de una carrera ingresado, retorna -1 si no se encuentra
        band = True
        i = 0
        ver = -1
        while band and i<len(self.__arreglo):
            if carrera == self.__arreglo[i].getNombreCarrera(carrera):
                ver = i
                band = False
            i += 1
        return ver
    def buscarCodigoCarrera(self, carrera):         #Busca el codigo de una Carrera segun su nombre
        text = ''
        band = True
        i = 0
        while band and i<len(self.__arreglo):
            if carrera == self.__arreglo[i].getNombreCarrera(carrera):
                text += '{}'.format(self.__arreglo[i].getCodigoCarrera(carrera))
                band = False
            i += 1
        return text
    def getDatosFacultad(self, codigo):         #Muestra los datos de una facultad segun su codigo
        text = ''
        band = True
        i = 0
        while band and i < len(self.__arreglo):
            if codigo == self.__arreglo[i].getCodFacultad():
                text += 'Codigo de Facultad: {} - {} - {}'.format(self.__arreglo[i].getCodFacultad(), self.__arreglo[i].getNomFacultad(), self.__arreglo[i].getLocalidad())
                band = False
            i += 1
        return text
