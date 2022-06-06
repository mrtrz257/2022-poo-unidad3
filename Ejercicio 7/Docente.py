from Personal import Personal

class Docente(Personal):
    __carrera = None
    __cargo = None
    __catedra = None
    def __init__(self, cuil, apellido, nombre, ant, sueldo, carrera='', cargo='', catedra='', area='', tipo='', categoria='', importe=0):
        super().__init__(cuil, apellido, nombre, ant, sueldo)
        self.__carrera = carrera
        self.__cargo = cargo
        self.__catedra = catedra
