class Carrera:
    __codigoCarrera = ''
    __nombreCarrera = ''
    __duracion = ''
    __titulo = ''
    __nivel = ''
    def __init__(self, codigoCar = '', nombreCar = '',titulo = '', duracion = '', nivel = ''):
        self.__codigoCarrera = str(codigoCar)
        self.__nombreCarrera = str(nombreCar)
        self.__titulo = str(titulo)
        self.__duracion = str(duracion)
        self.__nivel = str(nivel)
    def __str__(self):
        return '{} {} {} {} {}'.format(self.__codigoCarrera, self.__nombreCarrera,self.__titulo,  self.__duracion,self.__nivel)
    def getDatosCarrera(self):
        return '{} - Duración: {}'.format(self.__nombreCarrera, self.__duracion)
    def getCodigoCarrera(self):
        return self.__codigoCarrera
    def getNombreCarrera(self):
        return self.__nombreCarrera
    def getNivel(self):
        return self.__nivel
    def getDuracion(self):
        return self.__duracion
    def getTitulo(self):
        return self.__titulo
