class Heladera:
    __capacidadLitros = None
    __freezer = None
    __ciclica = None
    def __init__(self, marca, modelo, color, pais, precio, capac, freezer, ciclica):
        super().__init__(marca, modelo, color, pais, precio, capac, freezer, ciclica)
        self.__capacidadLitros = float(capac)
        self.__freezer = bool(freezer)
        self.__ciclica = bool(ciclica)
