from AparatoElectrico import AparatoElectrico
import json
from pathlib import  Path

class Heladera(AparatoElectrico):
    __capacidadLitros = None
    __freezer = None
    __ciclica = None
    def __init__(self, marca, modelo, color, pais, precio, capac, freezer, ciclica):
        super().__init__(marca, modelo, color, pais, precio)
        self.__capacidadLitros = float(capac)
        self.__freezer = bool(freezer)
        self.__ciclica = bool(ciclica)
    def __str__(self):
        return '{} {} {} {} {} {} {} {}'.format(super().getMarca(), super().getModelo(), super().getColor(), super().getPais(), super().getPrecio(), self.__capacidadLitros, self.__freezer, self.__ciclica)
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                marca=super().getMarca(),
                modelo=super().getModelo(),
                color=super().getColor(),
                pais=super().getPais(),
                precio=super().getPrecio(),
                capacidadLitros=self.__capacidadLitros,
                freezer=self.__freezer,
                ciclica=self.__ciclica
            )
        )
        return d
