class Calefactor:
    __marca = None
    __modelo = None
    def __init__(self, marca, modelo, potencia, matricula, calorias):
        self.__marca = str(marca)
        self.__modelo = str(modelo)
    def getMarca(self):
        return self.__marca
    def getModelo(self):
        return self.__modelo
