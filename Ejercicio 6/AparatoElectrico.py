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
