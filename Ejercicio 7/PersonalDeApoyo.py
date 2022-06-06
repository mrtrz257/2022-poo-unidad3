from Personal import Personal

class PersonalDeApoyo(Personal):
    __categoria = None
    def __init__(self, cuil, apellido, nombre, ant, sueldo, categoria):
        super().__init__(cuil, apellido, nombre, ant, sueldo)
        self.__categoria = str(categoria)
