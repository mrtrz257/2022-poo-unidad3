from AparatoElectrico import AparatoElectrico
import json
from pathlib import  Path

class Televisor(AparatoElectrico):
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
    def __str__(self):
        return '{} {} {} {} {} {} {} {} {}'.format(super().getMarca(), super().getModelo(), super().getColor(), super().getPais(), super().getPrecio(), self.__tipoPantalla, self.__pulgadas, self.__tipoDefinicion, self.__internet)
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                marca=super().getMarca(),
                modelo=super().getModelo(),
                color=super().getColor(),
                pais=super().getPais(),
                precio=super().getPrecio(),
                pantalla=self.__tipoPantalla,
                pulgadas=self.__pulgadas,
                definicion=self.__tipoDefinicion,
                internet=self.__internet
            )
        )
        return d
