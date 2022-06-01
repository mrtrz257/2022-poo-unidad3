from zope.interface import Interface

class InterfacesEjercicio5(Interface):
    def insertarElemento(self, posicion, objeto):
        pass
    def agregarElemento(self, objeto):
        pass
    def mostrarElemento(self, posicion):
        pass
