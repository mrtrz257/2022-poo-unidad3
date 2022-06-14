class AparatoElectrico:
    __marca = None
    __modelo = None
    __color = None
    __pais = None
    __precioBase = None
    def __init__(self, marca, modelo, color, pais, precio):
        self.__marca = str(marca)
        self.__modelo = str(modelo)
        self.__color = str(color)
        self.__pais = str(pais)
        self.__precioBase = float(precio)
    def __str__(self):
        return '{} {} {} {} {}'.format(self.__marca, self.__modelo, self.__color, self.__pais, self.__precioBase)
    def getMarca(self):
        return self.__marca
    def getModelo(self):
        return self.__modelo
    def getColor(self):
        return self.__color
    def getPais(self):
        return self.__pais
    def getPrecio(self):
        return self.__precioBase
