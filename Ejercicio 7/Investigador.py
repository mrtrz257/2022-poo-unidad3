from Personal import Personal

class Investigador(Personal):
    __areaInvestigacion = None
    __tipoInvestigacion = None
    def __init__(self, cuil, apellido, nombre, ant, sueldo, carrera='', cargo='', catedra='', area='', tipo='', categoria='', importe=0):
        super().__init__(cuil, apellido, nombre, ant, sueldo)
        self.__areaInvestigacion = str(area)
        self.__tipoInvestigacion = str(tipo)
