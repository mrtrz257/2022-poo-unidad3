class Televisor:
    __tipoPantalla = None
    __pulgadas = None
    __tipoDefinicion = None
    __internet = None
    def __init__(self, marca, modelo, color, pais, precio, tipoPant, pulg, tipoDef, internet):
        super().__init__(marca, modelo, color, pais, precio)
        self.__tipoPantalla = str(tipoPant)
        self.__pulgadas = int(pulg)
        self.__tipoDefinicion = str(tipoDef)
        self.__internet = bool(internet)
