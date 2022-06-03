class ManejadorJugadores:
    __lista = []
    def __init__(self):
        self.__lista = []
    def agregarJugador(self, unJugador):    #Agrega un jugador a la lista
        self.__lista.append(unJugador)
    def mostrarListaJugadores(self):    #Muestra toda la lista
        text = ''
        for elemento in self.__lista:
            text += '{} - {}\n'.format(elemento.getNombre(), elemento.getPais())
        return text
    def buscarJugador(self, jugador):   #Busca un jugador segun su nombre
        ver = -1
        i = 0
        band = True
        while band and i<len(self.__lista):
            if jugador == self.__lista[i].getNombre():
                ver = i
                band = False
            i += 1
        return ver
    def getJugador(self, jugad):    #Retorna un jugador segun su posicion
        return self.__lista[jugad]
