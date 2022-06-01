class Flores:
    __numero = ''
    __nombre = ''
    __color = ''
    __descripcion = ''
    __venta = 0
    def __init__(self, num, nombre, color, descrip):
        self.__numero = str(num)
        self.__nombre = str(nombre)
        self.__color = str(color)
        self.__descripcion = str(descrip)
        self.__venta = 0
    def __str__(self):
        return '{} - {} - {} - {}'.format(self.__numero, self.__nombre, self.__color, self.__descripcion)
    def getNumero(self):
        return self.__numero
    def getNombre(self):
        return self.__nombre
    def getColor(self):
        return self.__color
    def getDescripcion(self):
        return self.__descripcion
    def registraVenta(self):
        self.__venta += 1
    def getVenta(self):
        return self.__venta
    def __gt__(self, other):
        return self.__venta > other.getVenta()
