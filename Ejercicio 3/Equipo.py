from Contrato import Contrato

class Equipo:
    __nombre = ''
    __ciudad = ''
    __contratos = None
    def __init__(self, nom, ciudad):
        self.__nombre = str(nom)
        self.__ciudad = str(ciudad)
        self.__contratos = []
    def __str__(self):
        text = ' Equipo: '+self.__nombre + '  '
        return text
    def ContratarJugador(self, fechaInicio, fechaFin, sueldo, jugador):
        contrato = Contrato(fechaInicio, fechaFin, sueldo, jugador, self)
        self.__contratos.append(contrato)
    def mostrarContratos(self):
        for elemento in self.__contratos:
            print(elemento)
    def getNombre(self):
        return self.__nombre
    def getCiudad(self):
        return self.__ciudad
    def crearContrato(self, contrato):
        self.__contratos.append(contrato)
    def getContratos(self):
        return self.__contratos
