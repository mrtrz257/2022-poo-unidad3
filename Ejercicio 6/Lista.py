from zope.interface import implementer

from Nodo import Nodo
from Interfaces import Interfaces
from Televisor import Televisor
from Heladera import Heladera
from Lavarropa import Lavarropa

@implementer(Interfaces)

class Manejador:
    __comienzo = None
    def __init__(self):
        self.__comienzo = None
    def agregarElemento(self, aparato):
        nodo = Nodo(aparato)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
    def mostarElemento(self, pos):
        text = ''
        i = 0
        aux = self.__comienzo
        while aux.getSiguiente() != None and i < pos:
            i += 1
            aux = aux.getSiguiente()
        if i == pos:
            text += '{}'.format(aux.getDato())
            return text
        else:
            raise IndexError
    def listarDatos(self):
        aux = self.__comienzo
        while aux != None:
            dato = aux.getDato()
            print('Marca: {} - Pais de Origen: {} - Precio: {}'.format(dato.getMarca(), dato.getPais(), dato.getPrecio()))
            aux = aux.getSiguiente()
    def crearLista(self):
        lista = []
        aux = self.__comienzo
        while aux != None:
            dato = aux.getDato()
            lista.append(dato.toJSON())
            aux = aux.getSiguiente()
        return lista
    def mostrarSegunMarca(self):
        cont = 0
        aux = self.__comienzo
        while aux != None:
            dato = aux.getDato()
            if dato.getMarca()=='Phillips':
                cont += 1
            aux = aux.getSiguiente()
        return cont
    def mostrarSegunCarga(self):
        text = ''
        aux = self.__comienzo
        while aux != None:
            dato = aux.getDato()
            if isinstance(dato, Lavarropa):
                if dato.getCarga() == "Superior":
                    text += "{}\n".format(dato.getMarca())
            aux = aux.getSiguiente()
        return text
    def toJson(self):
        d = dict(
            __class__ = self.__class__.__name__,
            aparatos = self.crearLista()
        )
        return d
