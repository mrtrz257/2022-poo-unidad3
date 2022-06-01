class Ramo:
    __tamano = ''
    __flores = []
    def __init__(self, tam, flor = None, cantidad = 1):
        self.__tamano = str(tam)
        self.__flores = []
        if flor != None:
            self.addFlor(flor, cantidad)
    def addFlor(self, flor, cantidad = 1):
        for i in range(cantidad):
            self.__flores.append(flor)
    def __str__(self):
        text = 'Tamaño de Ramo: {} - Flores:\n'.format(self.__tamano)
        for elemento in self.__flores:
             text += '{}'.format(elemento) + '\n'
        return text
    def getTamanio(self):
        return self.__tamano
    def getFlor(self):
        return self.__flores