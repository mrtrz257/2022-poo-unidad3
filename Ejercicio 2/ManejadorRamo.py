from Ramo import Ramo

class ManejadorRamo:
    __lista = None
    __indice = -1
    def __init__(self):
        self.__lista = []
    def __str__(self):
        return '{}'.format(self.__lista)
    def CrearRamo(self, tam='', flores=None, cantidad = 1):     #Crea un ramo
        self.__indice += 1
        unRamo = Ramo(tam, flores, cantidad)
        self.__lista.append(unRamo)
        return self.__indice
    def agregarFlorARamo(self, indice, flor):   #Agrega una flor a la lista
        self.__lista[indice].addFlor(flor)
    def mostrarRamo(self):      #Muestra la lista entera
        text = ''
        for elemento in self.__lista:
            text += '{}'.format(elemento) + '\n'
        return text
    def mostrarRamoSegunTamano(self, tamanio):      #Muestra un ramo segun un tamaño ingresado por teclado
        text = ''
        for elemento in self.__lista:
            if tamanio == elemento.getTamanio():
                text += '{}\n'.format(elemento)
        return text
    def mostrarFlores(self):    #Muestra las flores de los ramos
        text = ''
        for elemento in self.__lista:
            text += '{}\n'.format(elemento.getFlor())
        return text
