class Lavarropa:
    __capacidadLavado = None
    __velCentrifugado = None
    __cantProgramas = None
    __tipoCarga = None
    def __init__(self, marca, modelo, color, pais, precio, capLav, VelCentr, cantProg, tipoCarga):
        super().__init__(marca, modelo, color, pais, precio, capLav, VelCentr, cantProg, tipoCarga)
        self.__capacidadLavado = int(capLav)
        self.__velCentrifugado = int(VelCentr)
        self.__cantProgramas = int(cantProg)
        self.__tipoCarga = str(tipoCarga)
