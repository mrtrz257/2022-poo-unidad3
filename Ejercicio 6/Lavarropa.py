from AparatoElectrico import AparatoElectrico
import json
from pathlib import  Path

class Lavarropa(AparatoElectrico):
    __capacidadLavado = None
    __velCentrifugado = None
    __cantProgramas = None
    __tipoCarga = None
    def __init__(self, marca, modelo, color, pais, precio, capLav, VelCentr, cantProg, tipoCarga):
        super().__init__(marca, modelo, color, pais, precio)
        self.__capacidadLavado = int(capLav)
        self.__velCentrifugado = int(VelCentr)
        self.__cantProgramas = int(cantProg)
        self.__tipoCarga = str(tipoCarga)
    def getCarga(self):
        return self.__tipoCarga
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                marca=super().getMarca(),
                modelo=super().getModelo(),
                color=super().getColor(),
                pais=super().getPais(),
                precio=super().getPrecio(),
                capacidadLavado=self.__capacidadLavado,
                velocidad=self.__velCentrifugado,
                programas=self.__cantProgramas,
                tipoCarga=self.__tipoCarga
            )
        )
        return d
