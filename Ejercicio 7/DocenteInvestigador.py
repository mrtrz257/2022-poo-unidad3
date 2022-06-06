from Docente import Docente
from Investigador import Investigador

class DocenteInvestigador(Docente, Investigador):
    __categoria = None
    __importeExtra = None
    def __init__(self, cuil, apellido, nombre, ant, sueldo, carrera, cargo, catedra,  area, tipo, categoria, importe):
        super().__init__(cuil, apellido, nombre, ant, sueldo, carrera, cargo, catedra,  area, tipo)
        self.__categoria = str(categoria)
        self.__importeExtra = float(importe)
    