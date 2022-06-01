class Jugador:
    __nombre = ''
    __dni = ''
    __ciudadNatal = ''
    __PaisDeOrigen = ''
    __FechaDeNacimiento = ''
    def __init__(self, nom, dni, ciudad, pais, fecha):
        self.__nombre = str(nom)
        self.__dni = str(dni)
        self.__ciudadNatal = str(ciudad)
        self.__PaisDeOrigen = str(pais)
        self.__FechaDeNacimiento = str(fecha)
    def __str__(self):
        text = ''
        text += self.__nombre+' \n'
        text += self.__dni+', '+self.__ciudadNatal+', '+self.__PaisDeOrigen+', '+self.__FechaDeNacimiento
        return text
    def getNombre(self):
        return self.__nombre
    def getPais(self):
        return self.__PaisDeOrigen
    def getDNI(self):
        return self.__dni
