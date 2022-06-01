class Contrato:
    __fechaInicio = ''
    __fechaFin = ''
    __pagoMensual = 0.0
    __jugador = None
    __equipo = None
    def __init__(self, fechaInicio, fechaFin, pago, jugador, equipo):
        self.__fechaInicio = str(fechaInicio)
        self.__fechaFin = str(fechaFin)
        self.__pagoMensual = float(pago)
        self.__jugador = jugador
        self.__equipo = equipo
    def __str__(self):
        text = ''
        text += '{}'.format(str(self.__jugador))
        text += '{}'.format(str(self.__equipo))
        text += '\nCONTRATO: Fecha Inicio: {} - Fecha Fin: {} - Sueldo: ${}'.format(self.__fechaInicio, self.__fechaFin, self.__pagoMensual)
        return text
    def getJugador(self):
        return self.__jugador
    def getEquipo(self):
        return self.__equipo
    def getFechaInicio(self):
        return self.__fechaInicio
    def getFechaFin(self):
        return self.__fechaFin
    def getPago(self):
        return self.__pagoMensual