class ManejadorJugadores:
    __lista = []
    def __init__(self):
        self.__lista = []
    def agregarJugador(self, unJugador):
        self.__lista.append(unJugador)
    def mostrarListaJugadores(self):
        text = ''
        for elemento in self.__lista:
            text += '{} - {}\n'.format(elemento.getNombre(), elemento.getPais())
        return text
    def buscarJugador(self, jugador):
        ver = -1
        i = 0
        band = True
        while band and i<len(self.__lista):
            if jugador == self.__lista[i].getNombre():
                ver = i
                band = False
            i += 1
        return ver
    def getJugador(self, jugad):
        return self.__lista[jugad]
