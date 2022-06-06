class Personal:
    __CUIL = None
    __apellido = None
    __nombre = None
    __antiguedad = None
    __sueldoBasico = None
    def __init__(self, cuil, apellido, nombre, ant, sueldo):
        self.__CUIL = str(cuil)
        self.__apellido = str(apellido)
        self.__nombre = str(nombre)
        self.__antiguedad = int(ant)
        self.__sueldoBasico = float(sueldo)
